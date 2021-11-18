from brain_games.cli import welcome_user


_quiz_dict = {}
_user_name = 'Player'


def set_questions_for_quiz(questions: tuple) -> None:
    """
    Set dictionary of questions for you quiz.

    Parameters
    ----------
    questions : tuple((str, str))

    Returns
    -------
    None, sets dictionary inside engine.
    Dictionary contains question: answer pairs.

    """
    global _quiz_dict
    _quiz_dict = {question: answer for question, answer in questions}


def _set_user_name():
    global _user_name
    _user_name = welcome_user()


def _print_hello_user():
    print(f'Hello, {_user_name}!')


def _print_welcome_title():
    print('Welcome to the Brain Games!')


def play_game():
    for question, answer in _quiz_dict.items():
        user_input = input(f'Question: {question}\nYour answer: ')
        if user_input == answer:
            print('Correct!')
        else:
            _game_over(user_input, answer)
    else:
        _end_game_player_wins()


def _end_game_player_wins():
    print(f'Congratulations, {_user_name}!')
    quit()


def _game_over(user_input, answer):
    print(f'{user_input!r} is wrong answer ;(. Correct answer was {answer!r}.')
    print(f'Let\'s try again, {_user_name}')
    quit()


def prepare_game_field():
    _print_welcome_title()
    _set_user_name()
    _print_hello_user()
