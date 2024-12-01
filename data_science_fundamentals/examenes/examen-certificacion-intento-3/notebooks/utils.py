"""
Herramientas de utilidades comúnmente usadas para el análisis de datos con Pandas, Matplotlib y Seaborn.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import re


def obtener_estadisticas_datos_nulos(df):
    qsna = df.shape[0] - df.isnull().sum(axis=0)
    qna = df.isnull().sum(axis=0)
    ppna = round(100 * (df.isnull().sum(axis=0) / df.shape[0]), 2)
    aux = {'datos sin NAs en q': qsna, 'Na en q': qna, 'Na en %': ppna}
    na = pd.DataFrame(data=aux)

    return na.sort_values(by='Na en %', ascending=False)


def variation_coefficient(series):
    return series.std() / series.mean()


def graficar_histogramas(
    df,
    columnas_df,
    nro_columnas=3,
    bins=5,
    kde=False,
    rotations=None,
    figsize=(14, 10)
):
    nro_filas = int(len(columnas_df) / nro_columnas)
    remanente = len(columnas_df) % nro_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=nro_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for columna in columnas_df:
        ax = axes[i_actual][j_actual]

        sns.histplot(df[columna], kde=kde, bins=bins, ax=ax)

        ax.set_title(f"Histograma {columna}")
        ax.set_xlabel(columna)
        ax.set_ylabel("Freq.")

        if rotations is not None and columna in rotations:
            ax.tick_params(axis='x', rotation=rotations[columna])

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()


def graficar_boxplots(df, columnas_df, nro_columnas=3, figsize=(14, 10)):
    nro_filas = int(len(columnas_df) / nro_columnas)
    remanente = len(columnas_df) % nro_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=nro_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for columna in columnas_df:
        ax = axes[i_actual][j_actual]

        sns.boxplot(df[columna], ax=ax)

        ax.set_title(f"Boxplot {columna}")

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()


def obtener_columnas_numericas_df(df):
    return df.select_dtypes(include=[np.number]).columns.tolist()


def obtener_columnas_categoricas_df(df):
    return df.select_dtypes(include=['string', 'object']).columns.tolist()


def obtener_estadisticas_descriptivas_df(df, num_decimales=None):
    campos_numericos = obtener_columnas_numericas_df(df)

    estadisticas = df[[*campos_numericos]].agg(
        [
            "min",
            "max",
            "mean",
            "std",
            "median",
            variation_coefficient,
        ]
    )

    if num_decimales is not None:
        estadisticas = estadisticas.round(2)

    return estadisticas


def obtener_estadisticas_descriptivas_df_es(df, num_decimales=None):
    estadisticas = obtener_estadisticas_descriptivas_df(
        df, num_decimales=num_decimales
    )

    estadisticas = estadisticas.T.rename(
        columns={
            "min": "Mínimo",
            "max": "Máximo",
            "mean": "Promedio",
            "std": "Desviación Estándar",
            "median": "Mediana",
            "variation_coefficient": "Coeficiente de Variación",
        }
    ).T

    return estadisticas


def graficar_histograma_y_boxplot(datos, nombre, bins=5):
    _, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    sns.histplot(datos, kde=True, bins=bins, ax=ax1)

    ax1.set_title(f"Histograma {nombre}")
    ax1.set_xlabel(nombre)
    ax1.set_ylabel("Freq.")

    sns.boxplot(datos, ax=ax2)

    ax2.set_title(f"Boxplot {nombre}")
    ax2.set_xlabel(nombre)

    plt.tight_layout()
    plt.show()


def obtener_diferencias_tipos_columnas(df, tipos_columnas_esperados):
    errores = []

    for columna, tipo_columna_esperado in tipos_columnas_esperados.items():
        if columna in df.columns:
            tipo_actual = str(df[columna].dtype)

            if not tipo_actual.startswith(tipo_columna_esperado):
                errores.append(
                    f"Error en columna '{columna}'. Tipo esperado es '{tipo_columna_esperado}' pero se encontró '{tipo_actual}'"
                )

        else:
            errores.append(
                f"Columna '{columna}' con tipo esperado '{tipo_columna_esperado}' no encontrado en dataframe."
            )

    return errores


def corregir_tipos_columnas(df, tipos_columnas_esperados):
    for columna, tipo in tipos_columnas_esperados.items():
        if columna in df.columns:
            try:
                if tipo.startswith("datetime"):
                    df[columna] = pd.to_datetime(df[columna], errors='coerce')
                else:
                    df[columna] = df[columna].astype(tipo)
            except Exception as e:
                print(
                    f"Error al convertir la columna '{columna}' a '{tipo}': {e}"
                )
    return df


def limpiar_cadena(cadena):
    """
    Función mostrada por el profesor.
    Limpia una cadena de texto realizando las siguientes operaciones:
    1. Convierte todo el texto a minúsculas.
    2. Elimina caracteres no imprimibles antes de la primera letra y después de la última letra,
       pero mantiene los caracteres internos.
    
    Parámetros:
    - cadena (str): La cadena de texto a limpiar.
    
    Retorna:
    - str: La cadena limpia.
    """
    if isinstance(cadena, str):
        # 1. Convertir todo a minúsculas
        cadena = cadena.lower()
        cadena = cadena.strip()

        return cadena
    return cadena


def graficar_histograma_con_datos_intercuartiles(
    df, columna, label, figsize=(15, 10)
):
    Q1 = np.percentile(df[columna], 25)
    Q2 = np.percentile(df[columna], 50)
    Q3 = np.percentile(df[columna], 75)
    IQR = Q3 - Q1

    plt.figure(figsize=figsize)
    plt.hist(
        df[columna], bins=20, color="skyblue", edgecolor="black", alpha=0.7
    )

    plt.axvline(
        Q1,
        color="orange",
        linestyle="dashed",
        linewidth=2,
        label=f"Q1 ({Q1:.2f})"
    )
    plt.axvline(
        Q2,
        color="red",
        linestyle="dashed",
        linewidth=2,
        label=f"Q2 (mediana) ({Q1:.2f})"
    )
    plt.axvline(
        Q3,
        color='purple',
        linestyle='dashed',
        linewidth=2,
        label=f"Q3 ({Q3:.2f})"
    )
    plt.axvspan(Q1, Q3, color="gray", alpha=0.3, label=f"IQR ({IQR:.2f})")

    plt.xlabel(label)
    plt.ylabel("Frecuencia")
    plt.title(f"Histograma de {columna} con índice intercuartil")
    plt.legend()
    plt.show()
