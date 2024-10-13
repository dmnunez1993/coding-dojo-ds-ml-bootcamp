"""
Resolución a Ejercicio Análisis de Datos con NumPy (Core)
"""
import numpy as np


def generar_datos_ventas(productos, tiendas, dias):
    # Genera datos de ventas aleatorias para el número de productos, tiendas y días especificados
    np.random.seed(0)
    return np.random.randint(0, 101, (productos, tiendas, dias))


def calcular_totales_ventas_por_producto(datos):
    # Calcula el total de ventas por producto a lo largo de la semana
    return np.sum(datos, axis=(1, 2))


def calcular_totales_ventas_por_tienda(datos):
    # Calcula el total de ventas por tienda a lo largo de la semana
    return np.sum(datos, axis=(0, 2))


def calcular_promedio_ventas_por_producto(datos):
    # Calcula el promedio de ventas por producto por día
    return np.mean(datos, axis=(1, 2))


def calcular_promedio_ventas_por_tienda(datos):
    # Calcula el promedio de ventas por tienda por día
    return np.mean(datos, axis=(0, 2))


def encontrar_producto_mayor_menor_ventas(totales_por_producto):
    # Encuentra el producto con mayor y menor ventas totales en la semana
    mayores_ventas = np.argmax(totales_por_producto)
    menores_ventas = np.argmin(totales_por_producto)

    return mayores_ventas, menores_ventas


def encontrar_tienda_mayor_menor_ventas(totales_por_tienda):
    # Encuentra la tienda con mayor y menor ventas totales en la semana
    mayores_ventas = np.argmax(totales_por_tienda)
    menores_ventas = np.argmin(totales_por_tienda)

    return mayores_ventas, menores_ventas


def main():
    productos = 10
    tiendas = 5
    dias = 7

    # Genera los datos de ventas

    datos = generar_datos_ventas(productos, tiendas, dias)
    print(datos)

    # Calcula los totales y promedios
    totales_por_producto = calcular_totales_ventas_por_producto(datos)
    totales_por_tienda = calcular_totales_ventas_por_tienda(datos)
    promedio_por_producto = calcular_promedio_ventas_por_producto(datos)
    promedio_por_tienda = calcular_promedio_ventas_por_tienda(datos)

    # Encuentra el producto y la tienda con mayor y menor ventas
    producto_mayor_ventas, producto_menor_ventas = encontrar_producto_mayor_menor_ventas(
        totales_por_producto
    )
    tienda_mayor_ventas, tienda_menor_ventas = encontrar_tienda_mayor_menor_ventas(
        totales_por_tienda
    )

    # Imprime los resultados
    print(
        "Total de ventas por producto a lo largo de la semana:",
        totales_por_producto
    )
    print(
        "Total de ventas por tienda a lo largo de la semana:",
        totales_por_tienda
    )
    print("Promedio de ventas por producto por día:", promedio_por_producto)
    print("Promedio de ventas por tienda por día:", promedio_por_tienda)
    print(f"Producto con mayor ventas: Producto {producto_mayor_ventas}")
    print(f"Producto con menor ventas: Producto {producto_menor_ventas}")
    print(f"Tienda con mayor ventas: Tienda {tienda_mayor_ventas}")
    print(f"Tienda con menor ventas: Tienda {tienda_menor_ventas}")


if __name__ == '__main__':
    main()
