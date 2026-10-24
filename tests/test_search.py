import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.items = [DigitalVideoDisc("The Lion King", "Animation", 19.95)]

    def test_exact_case_title_search(self) -> None:
        self.assertEqual(search_by_title(self.items, "Lion"), self.items)

    def test_title_search_is_case_insensitive(self) -> None:
        self.assertEqual(search_by_title(self.items, "lion"), self.items)

    def test_missing_title(self) -> None:
        self.assertEqual(search_by_title(self.items, "Star Wars"), [])


if __name__ == "__main__":
    unittest.main()
