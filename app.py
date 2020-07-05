
import random
from commerce import shipping
import commerce.shipping
from utils import find_max
import convert
from convert import kg_to_lbs
kg_to_lbs(100)


# Another method in Importing Modules
print(convert.kg_to_lbs(70))

numbers = [10, 3, 6, 2, 5, 1]
maximum = find_max(numbers)
print(maximum)


shipping.calc_shipping()
commerce.shipping.calc_shipping()

# Getting Random numbers
for i in range(4):
    print(random.randint(10, 20))
# choice Method in selecting  a Team lead
members = ["John", "Mary", "mosh"]
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 8)
        second = random.randint(1, 8)
        return first, second


dice = Dice()
print(dice.roll())
