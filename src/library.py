import json
import os
from typing import List, Optional


class Book:
    """
    Класс для создания отдельной книги
    """
    def __init__(
        self, id: int, title: str, author: str, year: int, status: str
    ) -> None:
        """
        Инициализация отдельной книги
        :param id: id книги
        :param title: название книги
        :param author: имя автора книги
        :param year: год издания книги
        :param status: статус книги
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """
        Метод для преобразования экземпляра класса в словарь
        :return: преобразованный экземпляр класса
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }


class Library:
    """
    Класс для работы с библиотекой книг.
    """
    def __init__(self, file_name: str = "books.json") -> None:
        """
        Инициализация библиотеки
        :param file_name: имя файла для хранения данных из библиотеки
        """
        self.books: List[Book] = []
        self.file_name = file_name
        self.load_file()

    def load_file(self) -> None:
        """
        Метод для загрузки данных из файла. Запускается при создании экземпляра класса
        """
        if os.path.exists(self.file_name):
            if os.path.getsize(self.file_name) == 0:
                with open(self.file_name, "w", encoding="utf-8") as file:
                    json.dump([], file, indent=4, ensure_ascii=False)
            with open(self.file_name, "r") as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]

    def save_data(self) -> None:
        """
        Метод для сохранения данных в файл. Если файл не существует - он будет создан
        """
        with open(self.file_name, "w") as file:
            json.dump(
                [book.to_dict() for book in self.books],
                file, indent=4,
                ensure_ascii=False
            )

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Метод для добавления книги в библиотеку. Id и статус генерируются автоматически
        :param title: Имя автора книги.
        :param author: Название книги.
        :param year: Год издания.
        """
        id = max((book.id for book in self.books), default=0) + 1
        self.books.append(Book(id, title, author, year, status="в наличии"))
        self.save_data()
        print(f"Книга {title} создана с {id = }")

    def find_book_for_id(self, id: int) -> Optional[Book]:
        """
        Метод поиска книг по id
        :param id: id книги
        :return: Книга удовлетворяющая критерию поиска
        """
        if id > 0:
            book = next((book for book in self.books if id == book.id), None)
            if book is None:
                print(f"Книги с {id = } не существует")
            else:
                return book
        else:
            print("id книги должен быть больше нуля")

    def remove_book(self, id: int) -> None:
        """
        Метод удаления книги по id
        :param id: id книги
        """
        book = self.find_book_for_id(id)
        if book:
            title = book.title
            self.books.remove(book)
            print(f"Удалена книга {title}")
            self.save_data()

    def search_book(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None,
    ) -> Optional[List[Book]]:
        """
        Метод для поиска книг по имени автора и/или названию книги и/или году издания
        :param title: Название книги
        :param author: Имя автора
        :param year: Год издания
        :return: Список книг
        """
        if author and title and year:
            return [
                book
                for book in self.books
                if book.author == author and
                   book.title == title and
                   book.year == year
            ]
        elif author and year:
            return [
                book
                for book in self.books
                if book.author == author and book.year == year
            ]
        elif author:
            return [book for book in self.books if book.author == author]
        elif title:
            return [book for book in self.books if book.title == title]
        elif year:
            return [book for book in self.books if book.year == year]

    def view_all_books(self) -> None:
        """
        Метод для отображения всех книг в библиотеке
        """
        if self.books:
            for book in self.books:
                print(", ".join(
                    f"{key}: {value}" for key, value in book.to_dict().items())
                )
        else:
            print("Библиотека пуста")

    def edit_status(self, id: int, status: str) -> None:
        """
        Метод для изиенения статуса книги
        :param id: id книги
        :param status: Статус, который будет установлен
        """
        book = self.find_book_for_id(id)
        if book:
            book.status = status
            print(f"Статус книги {book.title} изменен на '{status}'")
            self.save_data()
