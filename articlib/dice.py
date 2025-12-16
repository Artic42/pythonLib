import random


class dice:
    def __init__(self, size: int = 6) -> None:
        self.size = size

    def setSize(self, size: int) -> None:
        self.size = size

    def roll(self) -> int:
        return random.randint(1, self.size)


class customDice():
    def __init__(self, faces: list[str]) -> None:
        self.faces: list[str] = faces
        self.size: int = len(faces)

    def roll(self) -> str:
        face: str = random.choice(self.faces)
        return face


class dicePool:
    def __init__(self, diceList) -> None:
        self.diceList = diceList

    def roll(self) -> list[int]:
        return [d.roll() for d in self.diceList]

    def rollSum(self) -> int:
        return sum(self.roll())

    def rollSuccesses(self, target: int) -> int:
        return sum([1 for roll in self.roll() if roll >= target])
