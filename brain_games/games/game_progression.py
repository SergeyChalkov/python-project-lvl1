import random


def _get_sequence():
    def get_progression():
        start, step = random.randint(1, 50), random.randint(2, 9)
        max_index_in_progression = random.randint(6, 11)
        end_of_range = start + step * max_index_in_progression
        progression = list(num for num in range(start, end_of_range + 1, step))
        return progression, max_index_in_progression

    progression, max_index_in_progression = get_progression()
    position_for_hide = random.randint(0, max_index_in_progression)
    answer = str(progression[position_for_hide])
    progression[position_for_hide] = ".."
    question = " ".join(str(num) for num in progression)
    return question, answer


def get_quiz_questions(number_of_rounds: int = 3) -> tuple:
    """Creates a tuple of tuples with (question, answer) pairs for a quiz
    Args:
        number_of_rounds (int): how many times the function will be called,
            so the number of inner tuples == the number of game rounds
                (default is 3)

    Returns:
        tuple: a tuple of tuples: ((str, str), ..., (str, str))
    """
    return tuple((_get_sequence() for _ in range(number_of_rounds)))
