import random


GAME_RULES = "What number is missing in the progression?"


def _generate_progression(first, diff, length):
    end_of_range = first + diff * length
    progression = list(num for num in range(first, end_of_range + 1, diff))
    return progression


def get_question():
    first, diff = random.randint(1, 50), random.randint(2, 9)
    length = random.randint(6, 11)
    progression = _generate_progression(first, diff, length)
    position_for_hide = random.randint(0, length)
    answer = str(progression[position_for_hide])
    progression[position_for_hide] = ".."
    question = " ".join(str(num) for num in progression)
    return question, answer
