import random


GAME_RULES = "What number is missing in the progression?"


def _get_progression():
    start, step = random.randint(1, 50), random.randint(2, 9)
    max_index_in_progression = random.randint(6, 11)
    end_of_range = start + step * max_index_in_progression
    progression = list(num for num in range(start, end_of_range + 1, step))
    return progression, max_index_in_progression


def get_question():
    progression, max_index_in_progression = _get_progression()
    position_for_hide = random.randint(0, max_index_in_progression)
    answer = str(progression[position_for_hide])
    progression[position_for_hide] = ".."
    question = " ".join(str(num) for num in progression)
    return question, answer
