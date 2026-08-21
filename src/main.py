import json 
from pathlib import Path


def load_score_types():
    data_path = Path(__file__).parent.parent / "data" / "score_types.json"

    with open(data_path, "r", encoding="utf-8") as file: 
        data = json.load(file)

    return data["score_types"]

def find_score_type(score_types, score_type_id):
    for score_type in score_types:
        if score_type["id"] == score_type_id:
            return score_type

    return None

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

def main():
    score_types = load_score_types()

    while True:
        score_type = get_user_selection(score_types)

        if score_type is None:
            print()
            print("Hasta luego.")
            break

        print()
        print(f"Seleccionaste: {score_type['name']}")
        print()

if __name__ == "__main__":
    main()