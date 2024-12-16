import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


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


def calcular_metricas_modelo(
    modelo,
    x_test,
    y_test,
    nombre,
    calcular_roc_auc=False,
):
    y_pred = modelo.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    if calcular_roc_auc:
        y_pred_proba = modelo.predict_proba(x_test)[:, 1]
        roc_auc = roc_auc_score(y_test, y_pred_proba)

    print(f"Accuracy {nombre}: {accuracy}")
    print(f"Precision {nombre}: {precision}")
    print(f"Recall {nombre}: {recall}")
    print(f"F1 {nombre}: {f1}")

    if calcular_roc_auc:
        print(f"ROC AUC {nombre}: {roc_auc}")


def calcular_resumen_metricas_modelos(
    modelos, x_test, y_test, nombres, calcular_roc_auc=False
):
    metricas = []

    for modelo in modelos:
        y_pred = modelo.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        metricas_modelo = {
            "Accuracy": accuracy,
            "Precision": precision,
            "Recall": recall,
            "F1-Score": f1,
        }

        if calcular_roc_auc:
            y_pred_proba = modelo.predict_proba(x_test)[:, 1]
            roc_auc = roc_auc_score(y_test, y_pred_proba)
            metricas_modelo["ROC-AUC"] = roc_auc

        metricas.append(metricas_modelo)

    results = pd.DataFrame(
        metricas,
        index=nombres,
    )
    print(results)

    print("\n")

    print("Mejores modelos por métrica:\n")
    print(results.idxmax(axis=0))
