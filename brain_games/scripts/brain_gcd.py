#!/usr/bin/env python
from brain_games.games.quiz_engine import start_quiz_game
from brain_games.games.quiz_logic import get_quiz_questions


def main():
    start_quiz_game(quiz_rules, quiz_questions)


quiz_rules = "Find the greatest common divisor of given numbers."
quiz_questions = get_quiz_questions('brain-gcd')

if __name__ == '__main__':
    main()
