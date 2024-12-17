"""
Herramientas de utilidades comúnmente usadas para el análisis de datos con Pandas.
"""
import matplotlib.pyplot as plt
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


def graficar_histogramas(df, columnas_df, nro_columnas=3, bins=5, kde=False, rotations=None, figsize=(14, 10)):
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

    plt.show()
