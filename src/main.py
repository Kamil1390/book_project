from library import Library
import utils

def main() -> None:
    """
    Основная функция
    """
    library = Library()
    while True:
        utils.menu()
        choice = utils.correct_choice()
        if choice == "1":
            utils.add_book(library)
        elif choice == "2":
            utils.remove_book(library)
        elif choice == "3":
            utils.search_book(library)
        elif choice == "4":
            utils.view_all_books(library)
        elif choice == "5":
            utils.edit_status(library)
        elif choice == "0":
            print("Приходите еще")
            break
if __name__ == "__main__":
    main()
