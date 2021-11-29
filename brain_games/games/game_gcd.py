import math
import random


GAME_RULES = "Find the greatest common divisor of given numbers."


def get_question():
    number_one, number_two = random.randint(1, 1000), random.randint(1, 1000)
    answer = math.gcd(number_one, number_two)
    return f"{number_one} {number_two}", str(answer)
