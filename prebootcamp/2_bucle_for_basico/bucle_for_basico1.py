"""Módulo que implementa la tarea de Python Fundamentals / Bucles For: Basico 1"""


def ejecutar_ejercicio_1():
    """
    Implementa el ejercicio 1
    """
    for n in range(0, 101):
        print(n)


def ejecutar_ejercicio_2():
    """
    Implementa el ejercicio 2
    """
    for n in range(2, 501, 2):
        print(n)


def ejecutar_ejercicio_3():
    """
    Implementa el ejercicio 3
    """
    for n in range(1, 101):
        if n % 10 == 0:
            print("baby")
        elif n % 5 == 0:
            print("ice ice")
        else:
            print(n)


def ejecutar_ejercicio_4():
    """
    Implementa el ejercicio 4
    """
    suma = 0
    for n in range(0, 500001, 2):
        suma += n

    print(f"Suma de nros pares de 0 a 500000: {suma}")


def ejecutar_ejercicio_5():
    """
    Implementa el ejercicio 5
    """

    for n in range(2024, -1, -3):
        print(n)


def contador_dinamico(numInicial: int, numFinal: int, multiplo: int):
    """
    Contador dinámico que imprime los nros entre numInicial y numFinal
    si el nro es múltiplo de multiplo.

    :param int numInicial: Número inicial
    :param int numFinal: Número final
    :param int multiplo: Múltiplo
    """
    for n in range(numInicial, numFinal + 1):
        if n % multiplo == 0:
            print(n)


def ejecutar_ejercicio_6():
    """
    Implementa el ejercicio 6
    """
    numInicial = 3
    numFinal = 10
    multiplo = 2

    contador_dinamico(numInicial, numFinal, multiplo)


def main():
    """
    Función Principal
    """
    # ejecutar_ejercicio_1()
    # ejecutar_ejercicio_2()
    # ejecutar_ejercicio_3()
    # ejecutar_ejercicio_4()
    # ejecutar_ejercicio_5()
    ejecutar_ejercicio_6()


if __name__ == '__main__':
    main()
