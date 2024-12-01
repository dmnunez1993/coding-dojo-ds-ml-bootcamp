"""
Utilidades de estadísticas para dataframes.
"""
from scipy.stats import shapiro, normaltest


def realizar_prueba_shapiro(df, columnas):
    for columna in columnas:
        stat, p = shapiro(df[columna])

        texto_distribucion = "Normal"

        # Referencia: https://www.youtube.com/watch?v=IW1BMGtz6UY
        if p <= 0.05:
            texto_distribucion = "No normal"

        print(
            f"Columna {columna}: stat={stat} p={p} distribucion='{texto_distribucion}'"
        )


def realizar_prueba_d_agostino(df, columnas):
    for columna in columnas:
        stat, p = normaltest(df[columna])

        texto_distribucion = "Normal"

        # Referencia: https://www.youtube.com/watch?v=IW1BMGtz6UY
        if p <= 0.05:
            texto_distribucion = "No normal"

        print(
            f"Columna {columna}: stat={stat} p={p} distribucion='{texto_distribucion}'"
        )
