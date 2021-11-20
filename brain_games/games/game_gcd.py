from random import randint


def _get_numbers_for_quiz():
    numbers = randint(1, 1000), randint(1, 1000)
    answer = _get_gcd(sorted(numbers))
    return ' '.join(str(number) for number in numbers), str(answer)


def _get_gcd(numbers):
    lesser, greater = numbers
    if 0 in numbers:
        return greater
    return _get_gcd((greater % lesser, lesser))


def get_quiz_questions():
    return tuple((_get_numbers_for_quiz() for _ in range(_number_of_rounds)))


_number_of_rounds = 3
