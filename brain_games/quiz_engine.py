from brain_games.cli import welcome_user


_quiz_dict = {}
_user_name = 'Player'


def start_quiz_game(quiz_rules, quiz_questions):
    _set_questions_for_quiz(quiz_questions)
    print('Welcome to the Brain Games!')
    _set_user_name()
    print(f'Hello, {_user_name}!')
    print(quiz_rules)
    _play_game()


def _set_questions_for_quiz(questions: tuple) -> None:
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


def _play_game():
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
