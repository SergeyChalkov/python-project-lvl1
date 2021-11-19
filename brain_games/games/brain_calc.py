from brain_games.engine import start_quiz_game
from random import choice, randint


def create_expression():
    number_one, number_two = randint(1, 100), randint(1, 100)
    operator = choice('-+*')
    expression = number_one, operator, number_two
    answer = calculate_result(*expression)
    return ' '.join(str(element) for element in expression), answer


def calculate_result(number_one, operator, number_two):
    if operator == '-':
        return str(number_one - number_two)
    elif operator == '+':
        return str(number_one + number_two)
    else:
        return str(number_one * number_two)


def get_quiz_questions():
    return tuple((create_expression() for _ in range(number_of_rounds)))


def main():
    start_quiz_game(quiz_rules, quiz_questions)


number_of_rounds = 3
quiz_rules = "What is the result of the expression?"
quiz_questions = get_quiz_questions()

if __name__ == '__main__':
    main()
