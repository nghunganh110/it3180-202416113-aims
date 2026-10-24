import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class SearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.items = [DigitalVideoDisc("The Lion King", "Animation", 19.95)]

    def test_exact_case_title_search(self) -> None:
        self.assertEqual(search_by_title(self.items, "Lion"), self.items)

    def test_title_search_is_case_insensitive(self) -> None:
        self.assertEqual(search_by_title(self.items, "lion"), self.items)

    def test_missing_title(self) -> None:
        self.assertEqual(search_by_title(self.items, "Star Wars"), [])

    def test_category_search(self) -> None:
        self.assertEqual(search_by_category(self.items, "animation"), self.items)


if __name__ == "__main__":
    unittest.main()
