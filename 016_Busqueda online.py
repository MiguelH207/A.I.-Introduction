# Importamos la biblioteca requests para hacer solicitudes HTTP
import requests

def obtener_clima(ciudad, api_key):
    """
    Esta función obtiene el clima actual de una ciudad utilizando la API de OpenWeatherMap.

    Args:
        ciudad (str): El nombre de la ciudad para la cual se desea obtener el clima.
        api_key (str): La API key de OpenWeatherMap.

    Returns:
        dict: Un diccionario con la información del clima actual.
    """
    # URL de la API de OpenWeatherMap para obtener el clima actual de una ciudad
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'

    try:
        # Realizamos la solicitud GET a la URL
        response = requests.get(url)

        # Verificamos si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Convertimos la respuesta a formato JSON
            datos_clima = response.json()

            # Devolvemos los datos del clima como un diccionario
            return datos_clima
        else:
            # Si la solicitud no fue exitosa, mostramos un mensaje de error
            print(f"Error al obtener el clima de {ciudad}. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        # Si ocurre algún error durante la solicitud, mostramos un mensaje de error
        print(f"Error al obtener el clima de {ciudad}: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    ciudad = input("Ingrese el nombre de la ciudad: ")
    api_key = "your_api_key_here"  # Reemplaza "your_api_key_here" con tu API key de OpenWeatherMap
    clima = obtener_clima(ciudad, api_key)
    if clima is not None:
        temperatura = clima['main']['temp']
        descripcion = clima['weather'][0]['description']
        print(f"El clima en {ciudad} es {descripcion} con una temperatura de {temperatura}°C.")
