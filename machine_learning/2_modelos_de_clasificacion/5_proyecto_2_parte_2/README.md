# Análisis de preferencias de personas entre montañas y playas. Proyecto 2 Parte 1 (Core)

A través de este proyecto, se tiene como objetivo seleccionar un dataset para el proyecto 2 del curso de Machine Learning de Coding Dojo.

## Estructura

- `data/`: Contiene los datasets analizados
- `EDA/`: Contiene los notebook Jupyter usados para los EDAs para los 4 datasets
- `selected/`: Contiene el dataset y el notebook Jupyter del dataset seleccionado
- `README.md`: Este archivo

## Notebooks

- Notebook donde se lleva a cabo la Exploración del dataset 1: [EDA_dataset1_ads.ipynb](EDA/EDA_dataset1_ads.ipynb)
- Notebook donde se lleva a cabo la Exploración del dataset 2: [EDA_dataset2_phone_classification.ipynb](EDA/EDA_dataset2_phone_classification.ipynb)
- Notebook donde se lleva a cabo la Exploración del dataset 3: [EDA_dataset3_mountains_vs_beaches.ipynb](EDA/EDA_dataset3_mountains_vs_beaches.ipynb)
- Notebook donde se lleva a cabo la Exploración del dataset 4: [EDA_dataset4_titanic.ipynb](EDA/EDA_dataset3_mountains_vs_beaches.ipynb)

## Resúmenes

### EDA 1

Del EDA, se puede destacar lo siguiente

- El dataset es bueno para aplicar métodos de regresión, ya que solamente posee columnas numéricas.
- Según los histogramas, se puede notar que varias columnas no siguen una distribución estándar, por lo que se debe tener en cuenta en el escalado
- No existen muchos outliers, con la excepción de en la columna newspaper
- Existen correlaciones fuertes entre las columnas TV y radio en la cantidad de ventas, no tanto así en la columna de newspaper

### EDA 2

Del EDA, se puede destacar lo siguiente

- El dataset es bueno para aplicar métodos de clasificación, ya que la columna price_range es categórica.
- Según los histogramas, se puede notar que varias columnas no siguen una distribución estándar, por lo que se debe tener en cuenta en el escalado
- No existen muchos outliers, con la excepción de las columnas fc y px_height. Por este motivo, para el escalamiento de datos, tal vez lo mejor sería usar el RobustScaler
- Existen correlaciones fuertes entre las ram y price_range, y correlaciones un poco más débiles en battery_power, px_height, px_width.

### EDA 3

Del EDA, se puede destacar lo siguiente

- El dataset es bueno para aplicar métodos de clasificación binarias y multiclase
- Según los histogramas, se puede notar que varias columnas no siguen una distribución estándar, pero tampoco existen outliers. Por lo cual, se puede considerar el uso de MinMaxScaler para el esccalamiento.
- No existen outliers
- Existen correlaciones entre Preference con las columnas Proximity_to_Beaches y Proximity_to_Mountains
- Se puede notar una relación entre Preference Preferred_Activity y Age_Range (agrupación de columna Age por rango de edad)

### EDA 4

Del EDA, se puede destacar lo siguiente

- El dataset es bueno para aplicar métodos de clasificación binaria en la columna Survived
- Según los histogramas, se puede notar que varias columnas no siguen una distribución estándar, por lo que se debe tener en cuenta en el escalado
- Existe una gran cantidad de outliers en varias columnas, por lo que se debe tener en cuenta también a la hora de escalar
- Existen correlaciones entre las variables dependientes Fare, Age, Pclass, Sex, y la variable a predecir Survived

## Problema seleccionado

El problema seleccionado es el de las preferencias del público entre ir a montañas o a playas. Inicialmente, los problemas que presentaban más columnas y por ende mayor desafío son el del titanic y el de las preferencias. No obstante, como generalmente se utiliza el dataset del titanic como ejemplo en los cursos de data science y machine learning, y ya existen muchos recursos en línea a la hora de crear un modelo de predicción para este dataset, se optó por el de las preferencias del público entre montañas y playas.

### Descripción del problema

Este conjunto de datos tiene como objetivo analizar las preferencias del público entre dos tipos de vacaciones populares: montañas y playas. Proporciona información sobre diversos factores demográficos y de estilo de vida que pueden influir en estas preferencias. Al explorar este conjunto de datos, los usuarios pueden aplicar múltiples técnicas de aprendizaje automático para predecir si las personas prefieren montañas o playas en función de sus atributos.

## Instrucciones de uso

1. Clonar el repositorio: `git clone https://github.com/dmnunez1993/coding-dojo-ds-ml-bootcamp.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ir a la carpeta EDA en este proyecto y acceder a los notebooks jupyter de interés.

## Autores

Diego Maldonado

## Licencia

MIT
