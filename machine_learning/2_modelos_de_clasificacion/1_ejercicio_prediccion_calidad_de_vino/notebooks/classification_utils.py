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

    if labels is not None:
        ax.set_xticks(ticks=ax.get_xticks(), labels=labels)
        ax.set_yticks(ticks=ax.get_yticks(), labels=labels)
    plt.title("Matriz de Confusión")
    plt.show()
