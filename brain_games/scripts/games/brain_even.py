from brain_games.quiz_engine import start_quiz_game
from random import sample


def get_numbers_for_game():
    return ((number, is_even(number))
            for number in sample(range(1, 10000), k=number_of_rounds))


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    start_quiz_game(quiz_rules, quiz_questions)


number_of_rounds = 3
quiz_rules = "Answer 'yes' if the number is even, otherwise answer 'no'."
quiz_questions = get_numbers_for_game()

if __name__ == '__main__':
    main()
