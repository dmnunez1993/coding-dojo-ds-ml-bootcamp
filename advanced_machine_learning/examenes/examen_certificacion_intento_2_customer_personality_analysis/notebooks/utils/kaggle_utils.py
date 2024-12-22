"""
Utilidades para Kaggle
"""
import os

import opendatasets as od


def descargar_dataset_kaggle(url, camino_credenciales=None, data_dir='.'):
    if camino_credenciales is not None:
        if os.path.exists("./kaggle.json"):
            os.remove("./kaggle.json")
        os.symlink(camino_credenciales, "./kaggle.json")
    od.download(url, data_dir=data_dir)

    if camino_credenciales is not None:
        os.remove("./kaggle.json")
