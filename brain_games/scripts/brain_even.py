#!/usr/bin/env python
from brain_games.cli import welcome_user
from random import randrange


def print_title():
    print('Welcome to the Brain Games!')


def game_over(user_name, user_input, answer):
    print(f'{user_input!r} is wrong answer ;(. Correct answer was {answer!r}.')
    print(f'Let\'s try again, {user_name}')
    quit()


def player_wins(user_name):
    print(f'Congratulations, {user_name}!')
    quit()


def get_numbers_for_game():
    first_number = randrange(11, 99)
    second_number = randrange(100, 999)
    third_nimber = randrange(1000, 9999)
    return (first_number, second_number, third_nimber)


def play_even_number(user_name):
    all_numbers = get_numbers_for_game()
    for number in all_numbers:
        right_answer = 'no' if number % 2 else 'yes'
        user_input = input(f'Question: {number}\nYour answer: ')
        if user_input == right_answer:
            print('Correct!')
        else:
            game_over(user_name, user_input, right_answer)
    else:
        player_wins(user_name)


def main():
    print_title()
    user_name = welcome_user()
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_even_number(user_name)


if __name__ == '__main__':
    main()
