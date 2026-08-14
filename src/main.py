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

def main():
    """ 
    score_types = load_score_types()

    print("Tipos de puntuación psicométrica: \n")

    for score_type in score_types:
        print(f"- {score_type['name']}") 
        
        """
    
    score_types = load_score_types()

    score_type = find_score_type(score_types, "does_not_exist")

    if score_type:
        print(f"Encontrado: {score_type['name']}")
    else:
        print("Tipo de puntuación no encontrado")


if __name__ == "__main__":
    main()
