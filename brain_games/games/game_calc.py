import random

GAME_RULES = "What is the result of the expression?"


def _calculate_result(number_one, operator, number_two):
    if operator == "-":
        return number_one - number_two
    elif operator == "+":
        return number_one + number_two
    else:
        return number_one * number_two


def get_question():
    number_one, number_two = random.randint(1, 100), random.randint(1, 100)
    operator = random.choice("-+*")
    expression = number_one, operator, number_two
    answer = _calculate_result(*expression)
    return " ".join(str(element) for element in expression), str(answer)
