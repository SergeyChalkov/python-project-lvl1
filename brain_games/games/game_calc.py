import random


def _get_expression_for_calc():
    def _calculate_result(number_one, operator, number_two):
        if operator == "-":
            return str(number_one - number_two)
        elif operator == "+":
            return str(number_one + number_two)
        else:
            return str(number_one * number_two)

    number_one, number_two = random.randint(1, 100), random.randint(1, 100)
    operator = random.choice("-+*")
    expression = number_one, operator, number_two
    answer = _calculate_result(*expression)
    return " ".join(str(element) for element in expression), answer


def get_quiz_questions(number_of_rounds: int = 3) -> tuple:
    """Creates a tuple of tuples with (question, answer) pairs for a quiz
    Args:
        number_of_rounds (int): how many times the function will be called,
            so the number of inner tuples == the number of game rounds
                (default is 3)

    Returns:
        tuple: a tuple of tuples: ((str, str), ..., (str, str))
    """
    return tuple((_get_expression_for_calc() for _ in range(number_of_rounds)))
