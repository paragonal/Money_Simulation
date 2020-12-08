import random
from math import log, sinh

class Simulation():

    def __init__(self, num_agents, money_temperature):
        self.temperature = money_temperature
        self.agents = [Agent(starting_money=money_temperature) for x in range(num_agents)]
        self.fixing_constant = self.temperature*int(log(num_agents))

    def update(self, swaps, tax_rate = 0.1, tax_function = lambda x: sinh(4*x)/sinh(4)/4, welfare_threshold = 50):
        taxed_money = 0
        for i in range(swaps):
            amount = random.randint(1, self.temperature)

            a1 = random.choice(self.agents)
            a2 = random.choice(self.agents)
            while not a1.can_pay(a2, amount):
                a1 = random.choice(self.agents)
                a2 = random.choice(self.agents)

            a1.money -= amount
            taxed_money += amount * tax_rate
            a2.money += amount * (1-tax_rate)

        #redistribute all taxed money to poorest agents
        for agent in self.agents:
            tax = tax_function(agent.money/self.fixing_constant) * agent.money
            agent.money -= tax
            taxed_money += tax

        recipients = list(filter(lambda x: x.money < welfare_threshold, self.agents))
        for agent in recipients:
            agent.money += taxed_money/len(recipients)
            #print(len(recipients))
        #print(sum([x.money for x in self.agents]))

class Agent():
    def __init__(self, starting_money):
        self.money = starting_money

    def can_pay(self, other, amount):
        if self.money >= amount:

            return True

        return False
