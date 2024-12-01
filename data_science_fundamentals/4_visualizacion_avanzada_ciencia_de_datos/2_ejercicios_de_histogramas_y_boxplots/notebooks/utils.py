"""
Utilidades para dataset de Happiness.
Estas funciones fueron creadas para manejar todos los datasets.
"""
import matplotlib.pyplot as plt


def plot_histograms(df):
    # Configuración de tamaños encontrado aquí: https://scales.arabpsychology.com/stats/how-do-you-change-the-figure-size-of-a-pandas-histogram/
    fig = plt.figure(figsize=(20, 15))
    ax = fig.gca()

    df.hist(
        column=[
            "Happiness Score",
            "Economy (GDP per Capita)",
            "Health (Life Expectancy)",
            "Freedom",
        ],
        ax=ax,
        color='skyblue',
        edgecolor='black',
        alpha=0.7,
    )


def plot_boxplots(df):
    _, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

    ax1 = axes[0][0]
    ax2 = axes[0][1]
    ax3 = axes[1][0]
    ax4 = axes[1][1]

    ax1.boxplot(
        df["Happiness Score"],
        notch=False,
        patch_artist=True,
        boxprops=dict(facecolor='skyblue', color='black')
    )
    ax1.set_title("Boxplot de Happiness Score")
    ax1.set_ylabel("Scores")

    ax2.boxplot(
        df["Economy (GDP per Capita)"],
        notch=False,
        patch_artist=True,
        boxprops=dict(facecolor='skyblue', color='black')
    )
    ax2.set_title("Boxplot de Economy (GDP per Capita)")
    ax2.set_ylabel("Economy (GDP per Capita)")

    ax3.boxplot(
        df["Health (Life Expectancy)"],
        notch=False,
        patch_artist=True,
        boxprops=dict(facecolor='skyblue', color='black')
    )
    ax3.set_title("Boxplot de Health (Life Expectancy)")
    ax3.set_ylabel("Health (Life Expectancy)")

    ax4.boxplot(
        df["Freedom"],
        notch=False,
        patch_artist=True,
        boxprops=dict(facecolor='skyblue', color='black')
    )
    ax4.set_title("Boxplot de Freedom")
    ax4.set_ylabel("Freedom")

    plt.tight_layout()
    plt.show()


def plot_histogram_boxplot(
    df,
    nombre_columna,
    xlabel_hist=None,
    ylabel_hist=None,
    ylabel_boxplot=None,
):
    _, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))

    # ax1 = axes[0][0]
    # ax2 = axes[0][1]

    ax1.hist(
        df[nombre_columna],
        color='skyblue',
        edgecolor='black',
        alpha=0.7,
    )

    ax1.set_title(f"Histograma {nombre_columna}")

    if xlabel_hist is not None:
        ax1.set_xlabel(xlabel_hist)

    if ylabel_hist is not None:
        ax1.set_ylabel(ylabel_hist)

    ax2.boxplot(
        df[nombre_columna],
        notch=False,
        patch_artist=True,
        boxprops=dict(facecolor='skyblue', color='black')
    )
    ax2.set_title(f"Boxplot {nombre_columna}")

    if ylabel_boxplot:
        ax2.set_ylabel(ylabel_boxplot)

    plt.tight_layout()
    plt.show()
