import matplotlib.pyplot as plt
import seaborn as sns


def graficar_matriz_confusion(matriz_confusion, labels=None, figsize=(10, 8)):
    _, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    sns.heatmap(
        matriz_confusion,
        annot=True,
        cmap='Blues',
        center=0,
        ax=ax,
    )

    ax.set_xlabel("Predicción")
    ax.set_ylabel("Valores Reales")
    if labels is not None:
        ax.set_xticks(ticks=ax.get_xticks(), labels=labels)
        ax.set_yticks(ticks=ax.get_yticks(), labels=labels)
    plt.title("Matriz de Confusión")
    plt.show()


def graficar_matrices_confusion(
    matrices_confusion,
    nombres_matrices_confusion=None,
    labels=None,
    nro_columnas=3,
    figsize=(10, 8)
):
    nro_filas = int(len(matrices_confusion) / nro_columnas)
    remanente = len(matrices_confusion) % nro_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=nro_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for matriz_confusion in matrices_confusion:
        if nro_filas == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.heatmap(
            matriz_confusion,
            annot=True,
            cmap='Blues',
            center=0,
            ax=ax,
        )

        ax.set_xlabel("Predicción")
        ax.set_ylabel("Valores Reales")
        if labels is not None:
            ax.set_xticks(ticks=ax.get_xticks(), labels=labels)
            ax.set_yticks(ticks=ax.get_yticks(), labels=labels)

        if nombres_matrices_confusion is not None:
            nombre = nombres_matrices_confusion[i_actual * nro_columnas +
                                                j_actual]
            ax.set_title(f"Matriz de Confusión {nombre}")
        else:
            ax.set_title("Matriz de Confusión")

        j_actual += 1

        if j_actual >= nro_columnas:
            i_actual += 1
            j_actual = 0

    plt.show()
