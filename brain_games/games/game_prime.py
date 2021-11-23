import random


def _get_number_for_primes():
    def is_prime(number):
        if number in (0, 1) or not number % 2:
            return "no"
        if number in (2, 3, 5, 7):
            return "yes"
        max_divisor = int(number ** 0.5)
        divisors_list = [divisor for divisor in range(3, max_divisor + 1, 2)]
        for divisor in divisors_list:
            if not number % divisor:
                return "no"
        else:
            return "yes"

    number = random.randint(1, 1000)
    return str(number), is_prime(number)


def get_quiz_questions(number_of_rounds: int = 3) -> tuple:
    """Creates a tuple of tuples with (question, answer) pairs for a quiz
    Args:
        number_of_rounds (int): how many times the function will be called,
            so the number of inner tuples == the number of game rounds
                (default is 3)

    Returns:
        tuple: a tuple of tuples: ((str, str), ..., (str, str))
    """
    return tuple((_get_number_for_primes() for _ in range(number_of_rounds)))
