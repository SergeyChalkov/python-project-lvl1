#!/usr/bin/env python
import brain_games.engine
from brain_games.games.game_calc import get_question, GAME_RULES


def main():
    brain_games.engine.start_game(GAME_RULES, get_question)


if __name__ == "__main__":
    main()
