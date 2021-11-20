from random import sample


def get_quiz_questions():
    return ((number, _is_even(number))
            for number in sample(range(1, 10000), k=_number_of_rounds))


def _is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


_number_of_rounds = 3
