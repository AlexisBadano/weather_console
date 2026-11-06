import requests
from clima import obtener_coordenadas, obtener_clima
from interfaz import mostrar_clima

while True:
    print("\n===== WEATHER CONSOLE =====")
    print("1. Consultar clima de una ciudad")
    print("2. Salir")

    opcion = input("\nSeleccioná una opción: ")

    if opcion == "1":

        while True:
            ciudad = input("\nIngresá la ciudad: ")

            try:
                resultado = obtener_coordenadas(ciudad)

                if resultado is None:
                    print("La ciudad no se encontró.")
                    continue

                clima = obtener_clima(
                    resultado["latitud"],
                    resultado["longitud"]
                )

                mostrar_clima(clima, resultado)
                break

            except requests.exceptions.Timeout:
                print("Tiempo de espera agotado.")

            except requests.exceptions.ConnectionError:
                print("Error de conexión.")

            except requests.exceptions.HTTPError:
                print("Error al intentar acceder al servidor.")

            except requests.exceptions.JSONDecodeError:
                print("Surgió un error con la respuesta del servidor.")

            except requests.exceptions.RequestException:
                print("Ocurrió un error inesperado.")

    elif opcion == "2":
        print("\n¡Gracias por utilizar Weather Console!")
        break

    else:
        print("\nOpción inválida. Seleccioná 1 o 2.")