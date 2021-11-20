from random import randint


def get_progression_list():
    start, step = randint(1, 50), randint(2, 9)
    max_index_in_progression = randint(6, 11)
    end_of_progression = start + step * max_index_in_progression + 1
    progression = list(num for num in range(start, end_of_progression, step))
    return progression, max_index_in_progression


def create_q():
    progression, max_index_in_progression = get_progression_list()
    position_for_hide = randint(0, max_index_in_progression)
    answer = str(progression[position_for_hide])
    progression[position_for_hide] = '..'
    question = ' '.join(str(num) for num in progression)
    return question, answer


def get_quiz_questions():
    return tuple((create_q() for _ in range(3)))

print(get_quiz_questions())
