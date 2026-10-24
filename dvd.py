from dataclasses import dataclass


@dataclass(frozen=True)
class DigitalVideoDisc:
    title: str
    category: str = ""
    cost: float = 0.0
