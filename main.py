from cart import Cart
from dvd import DigitalVideoDisc


def main() -> None:
    cart = Cart()
    for title, cost in [("The Lion King", 19.95), ("Star Wars", 24.99), ("Aladdin", 18.95)]:
        cart.add_dvd(DigitalVideoDisc(title, "Animation", cost))
    print(f"Total cost: {cart.total_cost():.2f} $")


if __name__ == "__main__":
    main()
