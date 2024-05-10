import random

class dice:
    def __init__(self, size=6):
        self.size = size
        
    def setSize(self, size):
        self.size = size
        
    def roll(self):
        return random.randint(1, self.size)
    
class customDice(dice):
    def __init__(self, faces):
        self.faces = faces
        self.size = len(faces)
        
    def roll(self):
        return random.choice(self.faces)
    
class dicePool:
    def __init__(self, diceList):
        self.diceList = diceList
        
    def roll(self):
        return [d.roll() for d in self.diceList]
    
    def rollSum(self):
        return sum(self.roll())
    
    def rollSuccesses(self, target):
        return sum([1 for roll in self.roll() if roll >= target])