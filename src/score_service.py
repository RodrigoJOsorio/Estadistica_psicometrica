# Trabajar con los tipos de puntuación.
# Buscar, validar y obtener

def find_score_type(score_types, score_type_id):
    for score_type in score_types:
        if score_type["id"] == score_type_id:
            return score_type

    return None

def validate_score_type(score_type):
    required_fields = ["id", "name", "description"]

    for field in required_fields:
        if field not in score_type:
            return False

    return True
