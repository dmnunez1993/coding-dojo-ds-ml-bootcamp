"""Módulo que implementa la tarea de Python Fundamentals / Funciones Intermedias (Core)"""

from typing import List, Dict


def ejecutar_ejercicio_1():
    """
    Implementa el ejercicio 1
    """

    matriz = [[10, 15, 20], [3, 7, 14]]

    cantantes = [
        {
            "nombre": "Ricky Martin",
            "pais": "Puerto Rico"
        }, {
            "nombre": "Chayanne",
            "pais": "Puerto Rico"
        }
    ]

    ciudades = {
        "México": ["Ciudad de México", "Guadalajara", "Cancún"],
        "Chile": ["Santiago", "Concepción", "Viña del Mar"]
    }

    coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]

    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == 3:
                matriz[i][j] = 6

    for cantante in cantantes:
        if cantante["nombre"] == "Ricky Martin":
            cantante["nombre"] = "Enrique Martin Morales"

    print(cantantes)

    for _, ciudades_pais in ciudades.items():
        for idx in range(0, len(ciudades_pais)):
            if ciudades_pais[idx] == "Cancún":
                ciudades_pais[idx] = "Monterrey"

    print(ciudades)

    for coordenada in coordenadas:
        coordenada["latitud"] = 9.9355431

    print(coordenadas)


def iterarDiccionario(lista: List[Dict[str, str]]):
    """
    Itera sobre la lista e imprime el nombre y el país
    :param list lista: Lista de diccionarios
    """
    for el in lista:
        nombre = el["nombre"]
        pais = el["pais"]
        print(f"nombre - {nombre}, pais - {pais}")


def ejecutar_ejercicio_2():
    """
    Implementa el ejercicio 2
    """
    cantantes = [
        {
            "nombre": "Ricky Martin",
            "pais": "Puerto Rico"
        }, {
            "nombre": "Chayanne",
            "pais": "Puerto Rico"
        }, {
            "nombre": "José José",
            "pais": "México"
        }, {
            "nombre": "Juan Luis Guerra",
            "pais": "República Dominicana"
        }
    ]

    iterarDiccionario(cantantes)


def iterarDiccionario2(llave: str, lista: List[Dict[str, str]]):
    """
    Itera sobre la lista e imprime el valor correspondiente a la llave
    :param str llave: Llave a ser impresa
    :param list lista: Lista de diccionarios
    """

    for el in lista:
        valor = el[llave]
        print(valor)


def ejecutar_ejercicio_3():
    """
    Implementa el ejercicio 3
    """
    cantantes = [
        {
            "nombre": "Ricky Martin",
            "pais": "Puerto Rico"
        }, {
            "nombre": "Chayanne",
            "pais": "Puerto Rico"
        }, {
            "nombre": "José José",
            "pais": "México"
        }, {
            "nombre": "Juan Luis Guerra",
            "pais": "República Dominicana"
        }
    ]

    iterarDiccionario2("pais", cantantes)


def imprimirInformaccion(diccionario: Dict[str, List[str]]):
    """
    Itera sobre el diccionario e imprime los datos de cada clave.

    :param dict diccionario: Diccionario a ser recorrido
    """

    for llave, valores in diccionario.items():
        print(f"{len(valores)} {llave.upper()}")

        for valor in valores:
            print(valor)

        print("")


def ejecutar_ejercicio_4():
    """
    Implementa el ejercicio 4
    """
    costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas":
            ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }

    imprimirInformaccion(costa_rica)


def main():
    """
    Función Principal
    """
    ejecutar_ejercicio_1()
    ejecutar_ejercicio_2()
    ejecutar_ejercicio_3()
    ejecutar_ejercicio_4()


if __name__ == '__main__':
    main()
