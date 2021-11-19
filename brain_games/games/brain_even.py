from brain_games.engine import start_quiz_game
from random import sample


def get_numbers_for_game():
    return ((number, is_even(number))
            for number in sample(range(1, 10000), k=3))


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    start_quiz_game(quiz_rules, quiz_questions)


quiz_rules = "Answer 'yes' if the number is even, otherwise answer 'no'."
quiz_questions = get_numbers_for_game()

if __name__ == '__main__':
    main()
