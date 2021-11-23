import random


def _get_number_for_even():
    def _is_even(number):
        return "yes" if number % 2 == 0 else "no"

    number = random.randint(1, 1000)
    return str(number), _is_even(number)


def get_quiz_questions(number_of_rounds: int = 3) -> tuple:
    """Creates a tuple of tuples with (question, answer) pairs for a quiz
    Args:
        number_of_rounds (int): how many times the function will be called,
            so the number of inner tuples == the number of game rounds
                (default is 3)

    Returns:
        tuple: a tuple of tuples: ((str, str), ..., (str, str))
    """
    return tuple((_get_number_for_even() for _ in range(number_of_rounds)))
