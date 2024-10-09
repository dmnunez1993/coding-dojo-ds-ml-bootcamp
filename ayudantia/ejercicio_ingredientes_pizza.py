"""
Ejercicio de ayudanía de solicitud de pizza.
"""

INGREDIENTES_COMUNES = [
    "Mozarella",
    "Tomate",
]

PIZZAS_POR_TIPO = {
    "1": {
        "nombre": "Vegetariana",
        "ingredientes": ["Pimiento", "Tofu"]
    },
    "2":
        {
            "nombre": "No Vegetariana",
            "ingredientes": ["Peperoni", "Jamón", "Salmón"]
        }
}


def main():
    input_usuario = input(
        "Ingrese el tipo de pizza (1: Vegetariana, 2: No Vegetariana):"
    )

    while input_usuario not in PIZZAS_POR_TIPO:
        print("Tipo de pizza inválida. Por favor, vuelva a intentarlo")
        input_usuario = input(
            "Ingrese el tipo de pizza (1: Vegetariana, 2: No Vegetariana):"
        )

    ingredientes_pizza = PIZZAS_POR_TIPO[input_usuario]["ingredientes"]
    ingredientes_pizza_str = ""

    for idx, ingrediente in enumerate(ingredientes_pizza):
        ingredientes_pizza_str += f"{idx + 1}. {ingrediente}\n"

    print(f"Seleccione un ingrediente de la lista:\n{ingredientes_pizza_str}")
    ingrediente_seleccionado_str = input()

    while True:
        try:
            ingrediente_seleccionado_idx = int(ingrediente_seleccionado_str)

            if ingrediente_seleccionado_idx - 1 < len(ingredientes_pizza):
                break

        except ValueError:
            pass

        print("Ingrediente elegido inválido. Por favor, vuelva a intentarlo.")
        print(
            f"Seleccione un ingrediente de la lista:\n{ingredientes_pizza_str}"
        )
        ingrediente_seleccionado_str = input()

    tipo_pizza_seleccionada = PIZZAS_POR_TIPO[input_usuario]["nombre"]
    print(f"Tipo de pizza seleccionada: {tipo_pizza_seleccionada}")

    ingredientes_pizza = [
        ingredientes_pizza[ingrediente_seleccionado_idx - 1],
        *INGREDIENTES_COMUNES
    ]

    print("Ingredientes seleccionados:")

    for ingrediente in ingredientes_pizza:
        print(f"- {ingrediente}")


if __name__ == '__main__':
    main()
