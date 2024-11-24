from typing import Optional

from library import Library

def try_except_block(message: str) -> Optional[int]:
    """
    Функция для проверки корректности числовых значений id или год издания
    :param message: имя параметра
    :return: параметр в числовом виде
    """
    try:
        data = int(input(f"Введите {message.lower()}: "))
        return data
    except ValueError:
        print(f"{message} введен некорректно")

def add_book(library: Library) -> None:
    """
    Функция для добавления книги в библиотеку
    """
    title = input("Введите название книги: ")
    author = input("Введите имя автора книги: ")
    year = try_except_block("год издания")
    library.add_book(title, author, year) if year else None
    input("Для продолжения нажмите любую клавишу ")

def view_all_books(library: Library) -> None:
    """
    Функция для отображения всех книг из библиотеки
    """
    library.view_all_books()
    input("Для продолжения нажмите любую клавишу ")

def remove_book(library: Library) -> None:
    """
    Функция для удаления книги из библиотеки
    """
    id = try_except_block("id книги")
    library.remove_book(id) if id else None
    input("Для продолжения нажмите любую клавишу ")

def search_book(library: Library) -> None:
    """
     Функция для поиска книг по названию, автору и году издания
    """
    title = input("Введите название книги: ")
    author = input("Введите имя автора книги: ")
    year = try_except_block("год издания")
    books = library.search_book(title, author, year) if year else None
    if books:
        for book in books:
            print(", ".join(
                f"{key}: {value}" for key, value in book.to_dict().items()))
    else:
        print("По данным критериям книги не найдены")
    input("Для продолжения нажмите любую клавишу ")

def edit_status(library: Library) -> None:
    """
    Функция для изменения статуса книги
    """
    id = try_except_block("id книги")
    status = input("Введите статус книги: ")
    if status in ("в наличии", "выдана"):
        library.edit_status(id, status)
    else:
        print("Некорректный статус")
    input("Для продолжения нажмите любую клавишу ")

def menu() -> None:
    """
    Функция для прорисовки меню
    """
    print("\033[H\033[J", end="")
    print("=" * 20, "Добро Пожаловать В Библиотеку", "=" * 20)
    print("1 - Добавление книги")
    print("2 - Удаление книги")
    print("3 - Поиск книги")
    print("4 - Отображение всех книг")
    print("5 - Изменение статуса книги")
    print("0 - Выход из приложения")

def correct_choice() -> str:
    """
    Функция для проверки корректности введенного пользователем значения
    :return: корректный выбор пользователя
    """
    choice = input("Выберите нужное действие: ")
    while choice < "0" or choice > "5":
        choice = input("Введите клавишу от 0 до 5 включительно: ")
    return choice