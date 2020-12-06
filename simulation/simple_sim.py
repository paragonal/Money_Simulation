import random
from math import log

class Simulation():

    def __init__(self, num_agents, money_temperature):
        self.temperature = money_temperature
        self.agents = [Agent(starting_money=money_temperature) for x in range(num_agents)]
        self.fixing_constant = self.temperature*int(log(num_agents))

    def update(self, swaps):
        for i in range(swaps):
            amount = random.randint(1, self.temperature)
            while not random.choice(self.agents).pay(random.choice(self.agents), amount):
                pass




class Agent():
    def __init__(self, starting_money):
        self.money = starting_money

    def pay(self, other, amount):
        if self.money >= amount:
            self.money -= amount
            other.money += amount
            return True

        return False
