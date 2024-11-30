import requests


# Función para consumir los datos de la API
def fetch_data_from_api(api_url):
    response = requests.get(api_url, timeout=10)

    if response.status_code == 200:
        json_data = response.json()
    else:
        raise Exception(f"Error en la API: {response.status_code}")

    return json_data
