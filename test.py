import fractions
import random

first_number = fractions.Fraction(random.randint(1,9), 4)
second_number = fractions.Fraction(random.randint(1,9), 6)

print(first_number - second_number)