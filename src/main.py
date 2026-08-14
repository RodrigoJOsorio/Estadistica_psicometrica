import json 
from pathlib import Path


def load_score_types():
    data_path = Path(__file__).parent.parent / "data" / "score_types.json"

    with open(data_path, "r", encoding="utf-8") as file: 
        data = json.load(file)

    return data["score_types"]

def main():
    score_types = load_score_types()

    print("Tipos de puntuación psicométrica:")
    print()

    for score_type in score_types:
        print(f"- {score_type['name']}")


if __name__ == "__main__":
    main()
