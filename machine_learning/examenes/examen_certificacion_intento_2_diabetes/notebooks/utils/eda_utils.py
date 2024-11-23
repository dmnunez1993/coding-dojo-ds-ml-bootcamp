"""
Herramientas de utilidades comúnmente usadas para el análisis de datos con Pandas, Matplotlib y Seaborn.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def obtener_estadisticas_datos_nulos(df):
    qsna = df.shape[0] - df.isnull().sum(axis=0)
    qna = df.isnull().sum(axis=0)
    ppna = round(100 * (df.isnull().sum(axis=0) / df.shape[0]), 2)
    aux = {'datos sin NAs en q': qsna, 'Na en q': qna, 'Na en %': ppna}
    na = pd.DataFrame(data=aux)

    return na.sort_values(by='Na en %', ascending=False)


def variation_coefficient(series):
    return series.std() / series.mean()


def mode(series):
    return series.mode()


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
        if nro_filas == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        Q1 = np.percentile(df[columna].dropna(), 25)
        Q2 = np.percentile(df[columna].dropna(), 50)
        Q3 = np.percentile(df[columna].dropna(), 75)
        IQR = Q3 - Q1

        sns.histplot(df[columna], kde=kde, bins=bins, ax=ax)

        ax.axvline(
            Q1,
            color="orange",
            linestyle="dashed",
            linewidth=2,
            label=f"Q1 ({Q1:.2f})"
        )
        ax.axvline(
            Q2,
            color="red",
            linestyle="dashed",
            linewidth=2,
            label=f"Q2 (mediana) ({Q1:.2f})"
        )
        ax.axvline(
            Q3,
            color='purple',
            linestyle='dashed',
            linewidth=2,
            label=f"Q3 ({Q3:.2f})"
        )
        ax.axvspan(Q1, Q3, color="gray", alpha=0.3, label=f"IQR ({IQR:.2f})")

        ax.legend()

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
        if nro_filas == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.boxplot(df[columna], ax=ax)

        ax.set_title(f"Boxplot {columna}")

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()


def graficar_dispersiones(
    df, columnas_x, columna_y, nro_columnas=3, figsize=(14, 10)
):
    nro_filas = int(len(columnas_x) / nro_columnas)
    remanente = len(columnas_x) % nro_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=nro_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for columna in columnas_x:
        if nro_filas == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.scatterplot(df, x=columna, y=columna_y, ax=ax)

        ax.set_title(f"Dispersión {columna} vs {columna_y}")
        ax.set_xlabel(columna)
        ax.set_ylabel(columna_y)

        sns.regplot(
            x=columna,
            y=columna_y,
            data=df,
            scatter=False,
            color='red',
            line_kws={'linewidth': 2},
            ax=ax
        )

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()


def graficar_barras(
    df, columnas_x, columna_y, nro_columnas=3, figsize=(14, 10)
):
    nro_filas = int(len(columnas_x) / nro_columnas)
    remanente = len(columnas_x) % nro_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=nro_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for columna in columnas_x:
        if nro_filas == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.barplot(df, x=columna_y, y=columna, hue=columna_y, ax=ax)

        ax.set_title(f"Gráfico de barra {columna} vs {columna_y}")
        ax.set_xlabel(columna_y)
        ax.set_ylabel(columna)

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()


def graficar_barras_conteo(
    df,
    columnas_x,
    nro_columnas=3,
    figsize=(14, 10),
    rotations=None,
):
    nro_filas = int(len(columnas_x) / nro_columnas)
    remanente = len(columnas_x) % nro_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=nro_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for columna in columnas_x:
        df["counts"] = np.zeros(len(df))
        df_agrupado = df.groupby(columna)["counts"].count().reset_index()
        if nro_filas == 1 and nro_columnas == 1:
            ax = axes
        elif nro_filas == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.barplot(df_agrupado, x=columna, y="counts", hue=columna, ax=ax)

        ax.set_title(f"Gráfico de barra cant. {columna}")
        ax.set_xlabel(columna)
        ax.set_ylabel("Cant.")

        if rotations is not None:
            if columna in rotations:
                ax.tick_params(axis='x', rotation=rotations[columna])

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

        df.drop("counts", axis=1, inplace=True)

    plt.tight_layout()
    plt.show()


def graficar_barras_conteo_contra_columna(
    df,
    columnas_x,
    columna_y,
    nro_columnas=3,
    figsize=(14, 10),
    rotations=None,
):
    nro_filas = int(len(columnas_x) / nro_columnas)
    remanente = len(columnas_x) % nro_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=nro_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for columna in columnas_x:
        df["counts"] = np.zeros(len(df))
        df_agrupado = df.groupby([columna,
                                  columna_y])["counts"].count().reset_index()
        if nro_filas == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.barplot(df_agrupado, x=columna, y="counts", hue=columna_y, ax=ax)

        ax.set_title(f"{columna} vs {columna_y}")
        ax.set_xlabel(columna)
        ax.set_ylabel("Cant")

        if rotations is not None:
            if columna in rotations:
                ax.tick_params(axis='x', rotation=rotations[columna])

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

        df.drop("counts", axis=1, inplace=True)

    plt.tight_layout()
    plt.show()


def graficar_barras_promedio_contra_columna(
    df,
    columnas_x,
    columna_y,
    nro_columnas=3,
    figsize=(14, 10),
    rotations=None,
):
    nro_filas = int(len(columnas_x) / nro_columnas)
    remanente = len(columnas_x) % nro_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=nro_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for columna in columnas_x:
        df_agrupado = df.groupby([columna])[columna_y].mean().reset_index()
        if nro_filas == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.barplot(df_agrupado, x=columna, y=columna_y, hue=columna, ax=ax)

        ax.set_title(f"Gráfico de barra promedios. {columna} vs {columna_y}")
        ax.set_xlabel(columna)
        ax.set_ylabel(columna_y)

        if rotations is not None:
            if columna in rotations:
                ax.tick_params(axis='x', rotation=rotations[columna])

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()


def graficar_mapa_correlacion(
    df, columnas_de_interes, method='pearson', figsize=(14, 10)
):
    correlation_matrix = df[[*columnas_de_interes]].corr(method=method)
    print(correlation_matrix)
    # Crear un mapa de calor para la matriz de correlación de Pearson
    plt.figure(figsize=figsize)
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title("Mapa de Calor de la Correlación de Pearson")
    plt.show()


def obtener_columnas(df):
    return df.columns.tolist()


def obtener_columnas_numericas_df(df):
    return df.select_dtypes(include=[np.number]).columns.tolist()


def obtener_columnas_categoricas_df(df):
    return df.select_dtypes(include=[
        'string',
        'object',
        'category',
    ]).columns.tolist()


def obtener_estadisticas_descriptivas_df(df, num_decimales=None):
    campos_numericos = obtener_columnas_numericas_df(df)

    estadisticas = df[[*campos_numericos]].agg(
        [
            "count",
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


def obtener_datos_outliers_df(df):
    columnas_numericas = obtener_columnas_numericas_df(df)

    df_outliers = pd.DataFrame()

    for columna in columnas_numericas:
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1

        limite_minimo = Q1 - 1.5 * IQR
        limite_maximo = Q3 + 1.5 * IQR

        outliers = df[(df[columna] < limite_minimo) |
                      (df[columna] > limite_maximo)][columna]

        num_outliers = outliers.count()
        porcentaje_outliers = (outliers.count() / df[columna].count()) * 100

        df_outliers[columna] = {
            "Nro. Outliers": num_outliers,
            "Porc. Outliers": porcentaje_outliers,
            "Límite mínimo": limite_minimo,
            "Límite máximo": limite_maximo
        }

    return df_outliers


def obtener_estadisticas_descriptivas_df_es(df, num_decimales=None):
    estadisticas = obtener_estadisticas_descriptivas_df(
        df, num_decimales=num_decimales
    )

    estadisticas = estadisticas.T.rename(
        columns={
            "count": "Cantidad",
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
