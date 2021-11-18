#!/usr/bin/env python
import brain_games.engine as engine
from random import sample


def get_numbers_for_game():
    return ((number, is_even(number))
            for number in sample(range(1, 10000), k=3))


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    engine.set_questions_for_quiz(get_numbers_for_game())
    engine.prepare_game_field()
    print(how_to_play)
    engine.play_game()


how_to_play = "Answer 'yes' if the number is even, otherwise answer 'no'."

if __name__ == '__main__':
    main()
