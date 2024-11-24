import unittest
from unittest.mock import patch, MagicMock

from src.library import Library
from src.utils import add_book, remove_book, search_book, view_all_books, \
    try_except_block, edit_status, correct_choice


class TestUtilsCase(unittest.TestCase):
    def setUp(self):
        self.library = MagicMock(spec=Library)

    @patch(target="builtins.input")
    def test_try_except_block_valid(self, mock_input):
        mock_input.return_value="2024"
        result = try_except_block("год издания")
        self.assertEqual(result, 2024)

    @patch(target="builtins.input")
    @patch("builtins.print")
    def test_try_except_block_invalid(self, mock_print, mock_input):
        mock_input.return_value = "invalid"
        result = try_except_block("год издания")
        self.assertIsNone(result)
        mock_print.assert_called_once_with("год издания введен некорректно")

    @patch(target="builtins.input")
    def test_add_book(self, mock_input):
        mock_input.side_effect = ["Title", "Author", "2024", ""]
        add_book(self.library)
        self.library.add_book.assert_called_once_with("Title", "Author", 2024)

    @patch(target="builtins.input")
    def test_view_all_books(self, mock_input):
        mock_input.return_value = ""
        view_all_books(self.library)
        self.library.view_all_books.assert_called()

    @patch(target="builtins.input")
    def test_remove_book(self, mock_input):
        mock_input.side_effect = ["1", ""]
        remove_book(self.library)
        self.library.remove_book.assert_called_once_with(1)

    @patch(target="builtins.input")
    @patch(target="builtins.print")
    def test_search_book_valid(self, mock_print, mock_input):
        mock_input.side_effect = ["Title", "Author", "2024", ""]
        mock_bock = MagicMock()
        mock_bock.to_dict.return_value = {
            "id": 1,
            "title": "Title",
            "author": "Author",
            "year": 2024,
            "status": "в наличии",
        }
        self.library.search_book.return_value = [mock_bock]
        search_book(self.library)
        self.library.search_book.assert_called_once_with("Title", "Author", 2024)
        mock_print.assert_called_once_with(
            "id: 1, title: Title, author: Author, year: 2024, status: в наличии"
        )

    @patch(target="builtins.input")
    @patch(target="builtins.print")
    def test_search_book_invalid(self, mock_print, mock_input):
        mock_input.side_effect = ["Title", "Author", "2024", ""]
        self.library.search_book.return_value = []
        search_book(self.library)
        self.library.search_book.assert_called_once_with("Title", "Author", 2024)
        mock_print.assert_called_once_with(
            "По данным критериям книги не найдены"
        )

    @patch(target="builtins.input")
    def test_edit_status_valid(self, mock_input):
        mock_input.side_effect = ["1", "выдана", ""]
        edit_status(self.library)
        self.library.edit_status.assert_called_once_with(1, "выдана")

    @patch(target="builtins.input")
    @patch(target="builtins.print")
    def test_edit_status_invalid(self, mock_print, mock_input):
        mock_input.side_effect = ["1", "невыдана", ""]
        edit_status(self.library)
        self.library.edit_status.assert_not_called()
        mock_print.assert_called_once_with("Некорректный статус")

    @patch(target="builtins.input")
    def test_correct_choice(self, mock_input):
        mock_input.side_effect = ["6", "3"]
        result = correct_choice()
        self.assertEqual(result, "3")
