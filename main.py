from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims import __version__


def main() -> None:
    print(f"AIMS-mini v{__version__}")
    cart = Cart()
    for title, cost in [("The Lion King", 19.95), ("Star Wars", 24.99), ("Aladdin", 18.95)]:
        cart.add_dvd(DigitalVideoDisc(title, "Animation", cost))
    print(f"Total cost: {cart.total_cost():.2f} $")
    print(cart.print_cart())


if __name__ == "__main__":
    main()
