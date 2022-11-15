# генерирует людей

import random
import string
from model.human import Human

class HumanCreator:
    @staticmethod
    def create(size):
        NAMES = ("Alex", "Kate", "Mary", "Alice", "Peter",
                 "Ivan", "Sveta", "Ira", "Max", "Vova")

        MAX_AGE = 130
        MIN_AGE = 0

        ALFABET = string.ascii_uppercase

        ls = []

        for _ in range(size):
            firstname = random.choice(NAMES)
            surname = ALFABET[random.randrange(len(ALFABET))]
            age = random.randint(MIN_AGE, MAX_AGE)
            alive = random.randrange(2)
            human = Human(firstname, surname, age, alive)

            ls.append(human)

        return ls