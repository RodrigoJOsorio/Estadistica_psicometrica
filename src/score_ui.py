# Interacción usuario
def show_score_types(score_types):
    print("========================================")
    print("       ESTADÍSTICA PSICOMÉTRICA")
    print("========================================")
    print()
    print("Tipos de puntuación disponibles:")
    print()

    for number, score_type in enumerate(score_types, start=1):
        print(f"{number}. {score_type['name']}")

    print()
    print("0. Salir")
    print()


def get_user_selection(score_types):
    while True:
        show_score_types(score_types)

        option = input("Seleccione una opción: ")

        try:
            option = int(option)
        except ValueError:
            print()
            print("Entrada no válida. Introduzca un número.")
            print()
            continue

        if option == 0:
            return None

        if 1 <= option <= len(score_types):
            return score_types[option - 1]

        print()
        print("Opción fuera de rango.")
        print()

def show_score_type(score_type):
    print()
    print("========================================")
    print(f"          {score_type['name'].upper()}")
    print("========================================")
    print()

    print("Descripción:")
    print(score_type["description"])
    print()

    scale = score_type.get("scale")

    if scale and scale.get("min") is not None and scale.get("max") is not None:
        print("Escala:")
        print(f"{scale['min']} - {scale['max']}")
        print()

    show_classifications(score_type)

def show_classifications(score_type):
    interpretation = score_type.get("interpretation")

    if not interpretation:
        return

    classifications = interpretation.get("classifications")

    if not classifications:
        return

    print("Clasificaciones:")

    for classification in classifications:
        print(f"- {classification}")