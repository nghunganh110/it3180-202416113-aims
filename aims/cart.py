from aims.dvd import DigitalVideoDisc

MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self) -> None:
        self.items: list[DigitalVideoDisc] = []

    def add_dvd(self, dvd: DigitalVideoDisc) -> bool:
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")
        return True

    def total_cost(self) -> float:
        return round(sum(dvd.cost for dvd in self.items), 2)

    def total_cost_with_discount(self, percent: float) -> float:
        if not 0 <= percent <= 100:
            raise ValueError("Discount must be between 0 and 100 percent")
        return round(self.total_cost() * (1 - percent / 100), 2)

    def print_cart(self) -> str:
        if not self.items:
            return "The cart is empty"
        return "\n".join(
            f"{index}. {dvd.title} — {dvd.cost:.2f} $"
            for index, dvd in enumerate(self.items, start=1)
        )
