 # Weather Console 🌤️

## Descripción

Weather Console es una aplicación de consola desarrollada en Python que permite consultar las condiciones meteorológicas actuales de una ciudad ingresada por el usuario.

La aplicación utiliza la API de **Open-Meteo** para obtener información geográfica y meteorológica, y presenta los resultados mediante una interfaz visual utilizando Rich.

## Tecnologías y librerías

- **Python:** lenguaje de programación utilizado.
- **Requests:** para realizar solicitudes HTTP a la API.
- **Rich:** para diseñar y presentar la información en la terminal.
- **Open-Meteo:** servicio externo utilizado para obtener los datos meteorológicos.

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/AlexisBadano/weather_console
   ```

2. Ingresar a la carpeta del proyecto:

   ```bash
   cd weather_console
   ```

3. Crear el entorno virtual:

   ```bash
   python -m venv .venv
   ```

4. Activar el entorno virtual en Windows:

   ```powershell
   .venv\Scripts\activate
   ```

5. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Con el entorno virtual activado, ejecutar:

```bash
python main.py
```

## Funcionalidades

- Búsqueda de ciudades.
- Consulta de temperatura actual.
- Sensación térmica.
- Humedad relativa.
- Velocidad del viento.
- Descripción de las condiciones meteorológicas.
- Menú interactivo.
- Manejo de errores de conexión y respuestas del servidor.

## Integrantes

- Alexis Badano