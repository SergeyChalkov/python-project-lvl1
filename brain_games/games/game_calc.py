from random import choice, randint


def _create_expression():
    number_one, number_two = randint(1, 100), randint(1, 100)
    operator = choice('-+*')
    expression = number_one, operator, number_two
    answer = _calculate_result(*expression)
    return ' '.join(str(element) for element in expression), answer


def _calculate_result(number_one, operator, number_two):
    if operator == '-':
        return str(number_one - number_two)
    elif operator == '+':
        return str(number_one + number_two)
    else:
        return str(number_one * number_two)


def get_quiz_questions():
    return tuple((_create_expression() for _ in range(_number_of_rounds)))


_number_of_rounds = 3
