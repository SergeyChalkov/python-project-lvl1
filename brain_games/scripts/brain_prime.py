#!/usr/bin/env python
from brain_games.games.quiz_engine import start_quiz_game
from brain_games.games.quiz_logic import get_quiz_questions


def main():
    start_quiz_game(quiz_rules, quiz_questions)


quiz_rules = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
quiz_questions = get_quiz_questions('brain-prime')

if __name__ == '__main__':
    main()
