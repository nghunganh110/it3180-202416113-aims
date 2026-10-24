import unittest

from aims.cart import MAX_NUMBERS_ORDERED, Cart
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_total_cost(self) -> None:
        cart = Cart()
        for cost in (19.95, 24.99, 18.95):
            cart.add_dvd(DigitalVideoDisc("DVD", cost=cost))
        self.assertEqual(cart.total_cost(), 63.89)

    def test_add_dvd_until_full(self) -> None:
        cart = Cart()
        for index in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(index))))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("21st DVD")))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_print_empty_cart(self) -> None:
        self.assertEqual(Cart().print_cart(), "The cart is empty")

    def test_discount_returns_remaining_total(self) -> None:
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD", cost=100.0))
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_does_not_change_original_order(self) -> None:
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Zulu", cost=20.0))
        cart.add_dvd(DigitalVideoDisc("alpha", cost=10.0))
        self.assertEqual([dvd.title for dvd in cart.sort_by_title()], ["alpha", "Zulu"])
        self.assertEqual([dvd.cost for dvd in cart.sort_by_cost()], [10.0, 20.0])
        self.assertEqual(cart.items[0].title, "Zulu")


if __name__ == "__main__":
    unittest.main()
