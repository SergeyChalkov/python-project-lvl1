from random import randint, choice


def _get_greatest_common_divisor():
    def _get_gcd(numbers):
        lesser, greater = numbers
        if 0 in numbers:
            return greater
        return _get_gcd((greater % lesser, lesser))

    numbers = randint(1, 1000), randint(1, 1000)
    answer = _get_gcd(sorted(numbers))
    return " ".join(str(number) for number in numbers), str(answer)


def _get_expression_for_calc():
    def _calculate_result(number_one, operator, number_two):
        if operator == "-":
            return str(number_one - number_two)
        elif operator == "+":
            return str(number_one + number_two)
        else:
            return str(number_one * number_two)

    number_one, number_two = randint(1, 100), randint(1, 100)
    operator = choice("-+*")
    expression = number_one, operator, number_two
    answer = _calculate_result(*expression)
    return " ".join(str(element) for element in expression), answer


def _get_number_for_even():
    def _is_even(number):
        return "yes" if number % 2 == 0 else "no"

    number = randint(1, 1000)
    return str(number), _is_even(number)


def _get_sequence_for_progression():
    def get_progression():
        start, step = randint(1, 50), randint(2, 9)
        max_index_in_progression = randint(6, 11)
        end_of_range = start + step * max_index_in_progression
        progression = list(num for num in range(start, end_of_range + 1, step))
        return progression, max_index_in_progression

    progression, max_index_in_progression = get_progression()
    position_for_hide = randint(0, max_index_in_progression)
    answer = str(progression[position_for_hide])
    progression[position_for_hide] = ".."
    question = " ".join(str(num) for num in progression)
    return question, answer


def _get_number_for_primes():
    def is_prime(number):
        if number in (0, 1) or not number % 2:
            return "no"
        if number in (2, 3, 5, 7):
            return "yes"
        max_divisor = int(number ** 0.5)
        divisors_list = [divisor for divisor in range(3, max_divisor + 1, 2)]
        for divisor in divisors_list:
            if not number % divisor:
                return "no"
        else:
            return "yes"

    number = randint(1, 1000)
    return str(number), is_prime(number)


# Dictionary contains {game: function to call} pairs
_games_dict = {
    "brain-even": _get_number_for_even,
    "brain-calc": _get_expression_for_calc,
    "brain-gcd": _get_greatest_common_divisor,
    "brain-progression": _get_sequence_for_progression,
    "brain-prime": _get_number_for_primes,
}


def get_quiz_questions(game: str, number_of_rounds: int = 3) -> tuple:
    """Creates a tuple of tuples with (question, answer) pairs for a quiz
    Args:
        game (str): The name of the game. Use to call an associated function.
            Games available: brain-even, brain-calc, brain-gcd,
            brain-progression, brain-prime.
        number_of_rounds (int): how many times the function will be called,
            so the number of inner tuples == the number of game rounds
                (default is 3)

    Returns:
        tuple: a tuple of tuples: ((str, str), ..., (str, str))
    """
    questions = _games_dict[game]
    return tuple((questions() for _ in range(number_of_rounds)))
