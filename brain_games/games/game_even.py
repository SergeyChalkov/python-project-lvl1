import random


GAME_RULES = "Answer 'yes' if the number is even, otherwise answer 'no'."


def _is_even(number):
    return number % 2 == 0


def get_question():
    number = random.randint(1, 1000)
    return str(number), "yes" if _is_even(number) else "no"
