import requests


descripciones_clima = {
    0: "Cielo despejado",
    1: "Mayormente despejado",
    2: "Parcialmente nublado",
    3: "Cubierto",
    45: "Niebla",
    48: "Niebla con escarcha",
    51: "Llovizna ligera",
    53: "Llovizna moderada",
    55: "Llovizna intensa",
    56: "Llovizna helada ligera",
    57: "Llovizna helada intensa",
    61: "Lluvia ligera",
    63: "Lluvia moderada",
    65: "Lluvia intensa",
    66: "Lluvia helada ligera",
    67: "Lluvia helada intensa",
    71: "Nevada ligera",
    73: "Nevada moderada",
    75: "Nevada intensa",
    77: "Granos de nieve",
    80: "Chaparrones ligeros",
    81: "Chaparrones moderados",
    82: "Chaparrones intensos",
    85: "Chaparrones de nieve ligeros",
    86: "Chaparrones de nieve intensos",
    95: "Tormenta eléctrica",
    96: "Tormenta eléctrica con granizo ligero",
    97: "Tormenta eléctrica intensa",
    99: "Tormenta eléctrica con granizo intenso",
}

def interpretar_clima(codigo: int) -> str:
    """Recibe el codigo de la lista WMO de la api, busca la descrupcion en el diccionarion y la traduce a lo que significa en español"""

    resultado = descripciones_clima.get(codigo, "Codigo meteorologico desconocido")

    return resultado

URL_GEOCODIFICACION = "https://geocoding-api.open-meteo.com/v1/search"

def obtener_coordenadas(ciudad: str) -> dict | None:
    """Busca la ciudad y devuelve nombre, pais, longitud y latitud, arma el diccionario y lo devuelve o devuelve "None" si no la encuentra"""

    parametros = {
        "name": ciudad,
        "count": 1,
        "language": "es",
        "format": "json"
    }

    respuesta = requests.get(
        URL_GEOCODIFICACION,
        params=parametros,
        timeout=10
    )
    respuesta.raise_for_status()

    datos = respuesta.json()

    resultados_busqueda = datos.get("results")

    if not resultados_busqueda:
        
        return None


    ubicacion = {
        "nombre": resultados_busqueda[0]["name"],
        "pais": resultados_busqueda[0]["country"],
        "latitud": resultados_busqueda[0]["latitude"],
        "longitud": resultados_busqueda[0]["longitude"]
    }

    return ubicacion

URL_PRONOSTICO = "https://api.open-meteo.com/v1/forecast"

def obtener_clima(latitud: float, longitud: float) -> dict:
    """Recibe latitud y longitud y busca segun esas coordenadas los parametros que se le indican, arma el diccionario y lo devuelve"""


    parametros_clima = {
        "latitude": latitud,
        "longitude": longitud,
        "current": (
            "temperature_2m,"
            "apparent_temperature,"
            "relative_humidity_2m,"
            "wind_speed_10m,"
            "weather_code"
        ),
        "daily": (
            "weather_code,"
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_probability_max"
        ),
        "forecast_days": 3,
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "auto"
    }

    respuesta_clima = requests.get(
        URL_PRONOSTICO,
        params=parametros_clima,
        timeout=10
    )
    respuesta_clima.raise_for_status()

    datos_clima = respuesta_clima.json()
    
    clima_actual = {
        "temperatura": datos_clima["current"]["temperature_2m"],
        "sensacion_termica": datos_clima["current"]["apparent_temperature"],
        "humedad": datos_clima["current"]["relative_humidity_2m"],
        "viento": datos_clima["current"]["wind_speed_10m"],
        "codigo_clima": datos_clima["current"]["weather_code"],
        "descripcion_clima": interpretar_clima(datos_clima["current"]["weather_code"])
    }

    pronostico = []

    for i in range(1, 3):
        dia = {
            "fecha": datos_clima["daily"]["time"][i],
            "temperatura_maxima": datos_clima["daily"]["temperature_2m_max"][i],
            "temperatura_minima": datos_clima["daily"]["temperature_2m_min"][i],
            "probabilidad_lluvia": datos_clima["daily"]["precipitation_probability_max"][i],
            "codigo_clima": datos_clima["daily"]["weather_code"][i],
            "descripcion_clima": interpretar_clima(datos_clima["daily"]["weather_code"][i])
        }

        pronostico.append(dia)

    resultado = {
        "actual": clima_actual,
        "pronostico": pronostico
    }

    return resultado

    return clima_actual


    