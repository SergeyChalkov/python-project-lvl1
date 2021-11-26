import random


GAME_RULES = "Find the greatest common divisor of given numbers."


def _get_gcd(numbers):
    lesser, greater = numbers
    if 0 in numbers:
        return greater
    return _get_gcd((greater % lesser, lesser))


def get_question():
    numbers = random.randint(1, 1000), random.randint(1, 1000)
    answer = _get_gcd(sorted(numbers))
    return " ".join(str(number) for number in numbers), str(answer)
