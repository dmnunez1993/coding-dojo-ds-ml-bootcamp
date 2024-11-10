"""
Utilidades para Kaggle
"""
import os

import opendatasets as od


def descargar_dataset_kaggle(url, camino_credenciales, data_dir='.'):
    os.symlink(camino_credenciales, "./kaggle.json")
    od.download(url, data_dir=data_dir)
    os.remove("./kaggle.json")
