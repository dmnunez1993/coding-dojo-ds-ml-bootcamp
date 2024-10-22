import pandas as pd
import numpy as np

# Configuramos la semilla para reproducibilidad
np.random.seed(42)

# Generamos los datos sintéticos
user_id = range(1, 301)
app_version = np.random.choice(['1.0', '1.1', '1.2', '1.3'], 300)
platform = np.random.choice(['Android', 'iOS'], 300)
session_duration = np.random.randint(1, 180, 300)
number_of_sessions = np.random.randint(1, 20, 300)
country = np.random.choice(
    ['USA', 'Canada', 'Mexico', 'UK', 'Germany', 'France', 'Spain', 'Italy'],
    300
)
user_feedback = np.random.randint(1, 6, 300)

# Creamos el DataFrame
data = pd.DataFrame(
    {
        'user_id': user_id,
        'app_version': app_version,
        'platform': platform,
        'session_duration': session_duration,
        'number_of_sessions': number_of_sessions,
        'country': country,
        'user_feedback': user_feedback
    }
)

# Guardamos los datos en un archivo CSV
data.to_csv('../data/user_app_data.csv', index=False)
print("Datos generados y guardados en 'user_app_data.csv'")
