import math
import random


GAME_RULES = "Find the greatest common divisor of given numbers."


def _get_gcd(lesser, greater):
    if lesser == 0:
        return greater
    return _get_gcd(greater % lesser, lesser)


def get_question():
    number_one, number_two = random.randint(1, 1000), random.randint(1, 1000)
    if number_one > number_two:
        number_one, number_two = number_two, number_one
    answer = _get_gcd(number_one, number_two)
    return f"{number_one} {number_two}", str(answer)
