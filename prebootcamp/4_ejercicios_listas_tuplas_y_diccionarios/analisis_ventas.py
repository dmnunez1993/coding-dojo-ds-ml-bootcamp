"""Módulo que implementa la tarea de Python Fundamentals / 
Ejercicio Listas, Tuplas y diccionarios (Core)
"""
import csv
from datetime import datetime
from io import TextIOWrapper
import pathlib
import sys
from typing import List, Dict, Any, Tuple


def obtener_ingresos_totales(ventas: List[Dict[str, Any]]) -> float:
    """
    Obtiene los ingresos totales en los datos de ventas.

    :param list ventas: Ventas
    :rtype: float
    """
    ingresos_totales = 0.0

    for venta in ventas:
        ingresos_totales += venta["cantidad"] * venta["precio"]

    return ingresos_totales


def obtener_ventas_por_producto(ventas: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Obtiene las ventas por producto.

    :param list ventas: Ventas
    :rtype: dict
    """
    ventas_por_producto = {}

    for venta in ventas:
        if venta["producto"] not in ventas_por_producto:
            ventas_por_producto[venta["producto"]] = 0

        ventas_por_producto[venta["producto"]] += venta["cantidad"]

    return ventas_por_producto


def obtener_mas_vendidos(ventas_por_producto: Dict[str, int]) -> List[str]:
    """
    Obtiene los productos más vendidos

    :param dict ventas_por_producto: Cant. de ventas por producto
    :rtype: str
    """
    # En caso de que hayan más de un producto con la misma cant.
    # vendida, se enviarán todos
    mas_vendidos = []
    cant_mas_vendido = 0

    for nombre, cant in ventas_por_producto.items():
        if cant == cant_mas_vendido:
            mas_vendidos.append(nombre)
        elif cant > cant_mas_vendido:
            mas_vendidos = [
                nombre,
            ]
            cant_mas_vendido = cant

    return mas_vendidos


def obtener_precios_por_producto(
    ventas: List[Dict[str, Any]]
) -> Dict[str, Tuple[Any]]:
    """
    Obtiene los datos de precio por producto

    :param list ventas: Ventas
    :rtype: dict
    """
    precios_por_producto = {}

    for venta in ventas:
        if venta["producto"] not in precios_por_producto:
            precios_por_producto[venta["producto"]] = [0, 0]

        precios_por_producto[venta["producto"]
                            ][0] += venta["precio"] * venta["cantidad"]
        precios_por_producto[venta["producto"]][1] += venta["cantidad"]

    for producto, datos in precios_por_producto.items():
        precios_por_producto[producto] = tuple(datos)

    return precios_por_producto


def obtener_promedio_precios_por_producto(
    precios_por_producto: Dict[str, Tuple[Any]]
) -> Dict[str, float]:
    """
    Obtiene el promedio de venta por producto

    :param dict precios_por_producto: Precios por producto
    :rtype: dict
    """
    promedio_precios_por_producto = {}

    for producto, datos in precios_por_producto.items():
        total_ingresos = datos[0]
        cantidad_vendida = datos[1]
        if cantidad_vendida == 0:
            # Contemplar casos en los que se hayan vendido 0 productos
            promedio_precios_por_producto[producto] = 0
        else:
            promedio_precios_por_producto[producto
                                         ] = total_ingresos / cantidad_vendida

    return promedio_precios_por_producto


def obtener_ingresos_por_dia(ventas: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Obtiene los ingresos por día

    :param list ventas: Ventas
    :rtype: dict
    """
    ingresos_por_dia = {}

    for venta in ventas:
        if venta["fecha"] not in ingresos_por_dia:
            ingresos_por_dia[venta["fecha"]] = 0.0

        ingresos_por_dia[venta["fecha"]] += venta["cantidad"] * venta["precio"]

    return ingresos_por_dia


def obtener_resumen_ventas(
    precios_por_producto: Dict[str, Tuple[Any]],
    promedio_precios_por_producto: Dict[str, float],
) -> Dict[str, Dict[str, Any]]:
    """
    Obtiene los ingresos por día

    :param dict precios_por_producto: Precios por producto
    :param dict promedio_precios_por_producto: Promedio precios por producto
    :rtype: dict
    """

    resumen_ventas = {}

    for nombre_producto, datos_precios_producto in precios_por_producto.items():
        promedio = promedio_precios_por_producto.get(nombre_producto, 0.0)

        resumen_ventas[nombre_producto] = {
            "cantidad_total": datos_precios_producto[1],
            "ingresos_totales": datos_precios_producto[0],
            "precio_promedio": promedio
        }

    return resumen_ventas


def _imprimir_a_consola_y_archivo(texto: str, f: TextIOWrapper):
    print(texto)
    f.write(f"{texto}\n")


def main():
    """
    Función Principal
    """
    # Para este ejercicio, trabajar siempre en el directorio que contiene al script.
    # Se asume que el archivo ventas.csv está en el mismo directorio.
    directorio_script = pathlib.Path(__file__).parent
    camino_ventas = (directorio_script / "ventas.csv").resolve()
    # El resultado se guarda en el mismo directorio de ejecución
    # con nombre resultado_analisis_ventas.txt
    camino_resultados = (directorio_script /
                         "resultado_analisis_ventas.txt").resolve()
    ventas = []
    with open(camino_ventas, 'r', encoding="utf-8") as f:
        reader = csv.reader(
            f,
            delimiter=',',
        )

        primera_linea_consumida = False

        for row in reader:
            # Con este bloque se evita la lectura de la primera linea, que sería la cabecera del csv
            if not primera_linea_consumida:
                primera_linea_consumida = True
                continue

            # Prevenir procesamiento de líneas vacías
            if len(row) == 0:
                continue

            try:
                datetime.strptime(row[0], "%Y-%m-%d")
                ventas.append(
                    {
                        "fecha": row[0],
                        "producto": row[1],
                        "cantidad": int(row[2]),
                        "precio": float(row[3])
                    }
                )
            # En caso de que los datos no sean válidos, notificar y abandonar
            except ValueError:
                print(
                    "Datos inválidos, asegúrese de que ventas.csv esté formateado correctamente"
                )
                sys.exit(1)

    with open(camino_resultados, "w", encoding="utf-8") as f:
        ingresos_totales = obtener_ingresos_totales(ventas)

        _imprimir_a_consola_y_archivo(
            f"Ingresos totales: {ingresos_totales}", f
        )

        ventas_por_producto = obtener_ventas_por_producto(ventas)
        mas_vendidos = obtener_mas_vendidos(ventas_por_producto)

        # Tener en cuenta cantidad de vendidos para impresión
        if len(mas_vendidos) == 0:
            _imprimir_a_consola_y_archivo("No se encontraron ventas!", f)
        elif len(mas_vendidos) == 1:
            _imprimir_a_consola_y_archivo(
                f"Producto más vendido: {mas_vendidos[0]}",
                f,
            )
        else:
            _imprimir_a_consola_y_archivo(
                f"Productos más vendidos: {','.join(mas_vendidos)}",
                f,
            )

        precios_por_producto = obtener_precios_por_producto(ventas)

        promedio_precios_por_producto = obtener_promedio_precios_por_producto(
            precios_por_producto
        )

        _imprimir_a_consola_y_archivo(
            "\nPromedio de precios por producto:",
            f,
        )
        _imprimir_a_consola_y_archivo(
            "Producto\tPromedio",
            f,
        )

        for producto, promedio in promedio_precios_por_producto.items():
            _imprimir_a_consola_y_archivo(
                f"{producto}\t\t{promedio}",
                f,
            )

        ingresos_por_dia = obtener_ingresos_por_dia(ventas)

        ingresos_por_dia_lista = [
            {
                "fecha": fecha,
                "ingresos": ingresos
            } for fecha, ingresos in ingresos_por_dia.items()
        ]

        ingresos_por_dia_lista.sort(
            key=lambda x: datetime.strptime(x["fecha"], "%Y-%m-%d")
        )

        _imprimir_a_consola_y_archivo(
            "\nIngresos por día:",
            f,
        )
        _imprimir_a_consola_y_archivo(
            "Fecha\t\tIngresos",
            f,
        )

        for datos_ingresos_dia in ingresos_por_dia_lista:
            fecha = datos_ingresos_dia["fecha"]
            ingresos = datos_ingresos_dia["ingresos"]

            _imprimir_a_consola_y_archivo(
                f"{fecha}\t{ingresos}",
                f,
            )

        resumen_ventas = obtener_resumen_ventas(
            precios_por_producto,
            promedio_precios_por_producto,
        )

        _imprimir_a_consola_y_archivo(
            "\nResumen ventas:",
            f,
        )
        _imprimir_a_consola_y_archivo(
            "Producto\tCant. Total\tIngresos Totales\tPrecio Promedio",
            f,
        )

        for producto, datos_producto in resumen_ventas.items():
            cantidad_total = datos_producto["cantidad_total"]
            ingresos_totales = datos_producto["ingresos_totales"]
            precio_promedio = datos_producto["precio_promedio"]

            _imprimir_a_consola_y_archivo(
                f"{producto}\t\t{cantidad_total}\t\t{ingresos_totales}\t\t\t{precio_promedio}",
                f,
            )


if __name__ == '__main__':
    main()
