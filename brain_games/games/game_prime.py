import math
import random


GAME_RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def _is_prime(number):
    if number in {0, 1}:
        return False
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if not number % divisor:
            return False
    return True


def get_question():
    number = random.randint(1, 1000)
    return str(number), 'yes' if _is_prime(number) else 'no'
