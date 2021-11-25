import random


GAME_RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def _is_prime(number):
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


def get_question():
    number = random.randint(1, 1000)
    return str(number), _is_prime(number)
