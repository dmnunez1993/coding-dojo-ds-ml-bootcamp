"""
Herramientas de utilidades comúnmente usadas para el análisis de datos con Pandas.
"""
import pandas as pd


def obtener_estadisticas_datos_nulos(df):
    qsna = df.shape[0] - df.isnull().sum(axis=0)
    qna = df.isnull().sum(axis=0)
    ppna = round(100 * (df.isnull().sum(axis=0) / df.shape[0]), 2)
    aux = {'datos sin NAs en q': qsna, 'Na en q': qna, 'Na en %': ppna}
    na = pd.DataFrame(data=aux)

    return na.sort_values(by='Na en %', ascending=False)


def variation_coefficient(series):
    return series.std() / series.mean()
