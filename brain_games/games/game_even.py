import random


GAME_RULES = "Answer 'yes' if the number is even, otherwise answer 'no'."


def _is_even(number):
    return "yes" if number % 2 == 0 else "no"


def get_question():
    number = random.randint(1, 1000)
    return str(number), _is_even(number)