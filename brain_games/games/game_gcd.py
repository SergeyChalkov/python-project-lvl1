import random


def _get_gcd():
    def _get_gcd(numbers):
        lesser, greater = numbers
        if 0 in numbers:
            return greater
        return _get_gcd((greater % lesser, lesser))

    numbers = random.randint(1, 1000), random.randint(1, 1000)
    answer = _get_gcd(sorted(numbers))
    return " ".join(str(number) for number in numbers), str(answer)


def get_quiz_questions(number_of_rounds: int = 3) -> tuple:
    """Creates a tuple of tuples with (question, answer) pairs for a quiz
    Args:
        number_of_rounds (int): how many times the function will be called,
            so the number of inner tuples == the number of game rounds
                (default is 3)

    Returns:
        tuple: a tuple of tuples: ((str, str), ..., (str, str))
    """
    return tuple((_get_gcd() for _ in range(number_of_rounds)))
