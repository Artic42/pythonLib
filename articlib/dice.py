import random
import logging


log = logging.getLogger()


class dice:
    def __init__(self, size: int = 6, log: bool = True) -> None:
        self.log: bool = log
        self.size: int = size

    def setSize(self, size: int) -> None:
        self.size = size

    def setLog(self, log: bool) -> None:
        self.log = log

    def roll(self) -> int:
        result: int = random.randint(1, self.size)
        if self.log is True:
            log.info(f"Dice of size {self.size} rolled result is {result}")
        return result


class customDice():
    def __init__(self, faces: list[str], name: str, log: bool = True) -> None:
        self.faces: list[str] = faces
        self.name: str = name
        self.log: bool = log
        self.size: int = len(faces)

    def roll(self) -> str:
        face: str = random.choice(self.faces)
        if self.log is True:
            log.info(f"{self.name} dice roll result is {face}")
        return face


class dicePool:
    def __init__(self, diceList: list[dice], log: bool = True) -> None:
        self.log: bool = log
        self.diceList: list[dice] = diceList

    def roll(self) -> list[int]:
        result: list[int] = [d.roll() for d in self.diceList]
        if self.log is True:
            log.info(f"Dice pool rolled with the following result {result}")
        return result

    def rollSum(self) -> int:
        result: int = sum(self.roll())
        if self.log is True:
            log.info(f"Dice pool sum is {result}")
        return result

    def rollSuccesses(self, target: int) -> int:
        result: int = sum([1 for roll in self.roll() if roll >= target])
        if self.log is True:
            log.info(f"Roll dice pool looking for {target}, {result} successes")
        return result
