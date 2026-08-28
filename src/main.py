
from score_loader import load_score_types
from score_ui import get_user_selection, show_score_type

def main():
    score_types = load_score_types()

    while True:
        score_type = get_user_selection(score_types)

        if score_type is None:
            print()
            print("Hasta luego.")
            break

        show_score_type(score_type)

if __name__ == "__main__":
    main()
