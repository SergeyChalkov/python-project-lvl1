import random

GAME_RULES = "What is the result of the expression?"


def _calculate_result(number_one, operator, number_two):
    if operator == "-":
        return number_one - number_two
    elif operator == "+":
        return number_one + number_two
    elif operator == "*":
        return number_one * number_two


def generate_round():
    number_one, number_two = random.randint(1, 100), random.randint(1, 100)
    operator = random.choice("-+*")
    answer = _calculate_result(number_one, operator, number_two)
    return f"{number_one} {operator} {number_two}", str(answer)
