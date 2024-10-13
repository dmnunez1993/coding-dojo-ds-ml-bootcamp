"""
Solución a ejercicio Sistema de calficaciones (Core)
"""


def obtener_numero_estudiantes():
    # Pide al usuario el número de estudiantes y devuelve el valor
    while True:
        try:
            num_estudiantes = int(
                input("Indique el nro. de estudiantes (min. 1): ")
            )

            if num_estudiantes > 0:
                break
        except ValueError:
            pass

        print(
            "Nro de estudiantes introducidos inválido. Por favor, vuelva a intentar."
        )

    return num_estudiantes


def obtener_nombre_estudiante():
    # Pide al usuario el nombre del estudiante y devuelve el valor
    nombre_estudiante = input("Introduzca el nombre para el estudiante: ")

    return nombre_estudiante


def obtener_numero_asignaturas():
    # Pide al usuario el número de asignaturas y devuelve el valor
    while True:
        try:
            num_asignaturas = int(
                input("Introduzca el nro de asignaturas para el estudiante: ")
            )

            if num_asignaturas > 0:
                break
        except ValueError:
            pass

        print("Nro de asignaturas inválida. Por favor, vuelva a intentar.")

    return num_asignaturas


def obtener_calificaciones(num_asignaturas):
    # Pide al usuario las calificaciones para cada asignatura y las devuelve en una lista
    calificaciones = []
    for num_asignatura in range(0, num_asignaturas):
        while True:
            try:
                calificacion = int(
                    input(
                        f"Introduzca la califiación para la materia {num_asignatura + 1} del estudiante (0-10): "
                    )
                )

                if 0 <= calificacion <= 10:
                    break
            except ValueError:
                pass

            print("Calificación inválida. Por favor, vuelva a intentar")

        calificaciones.append(calificacion)

    return calificaciones


def calcular_promedio(calificaciones):
    # Calcula y devuelve el promedio de las calificaciones
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(promedio):
    # Determina si el estudiante ha aprobado o reprobado basándose en el promedio
    return promedio >= 6.0


def imprimir_resumen(estudiantes):
    # Imprime un resumen con el nombre de los estudiantes, su promedio y su estado
    print("\n")
    for idx, estudiante in enumerate(estudiantes):
        print(f"Resultados estudiante {idx + 1}: \n")

        nombre = estudiante["nombre"]
        promedio = estudiante["promedio"]
        estado = estudiante["estado"]
        estado_str = "Aprobado" if estado else "Reprobado"

        print(f"Nombre: {nombre}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Estado: {estado_str}")

        print("\n")


def main():
    num_estudiantes = obtener_numero_estudiantes()
    estudiantes = []

    for idx in range(num_estudiantes):
        print(f"Datos estudiante {idx + 1}")
        nombre = obtener_nombre_estudiante()
        num_asignaturas = obtener_numero_asignaturas()
        calificaciones = obtener_calificaciones(num_asignaturas)
        promedio = calcular_promedio(calificaciones)
        estado = determinar_estado(promedio)

        estudiantes.append(
            {
                'nombre': nombre,
                'promedio': promedio,
                'estado': estado
            }
        )

    imprimir_resumen(estudiantes)


if __name__ == '__main__':
    main()
