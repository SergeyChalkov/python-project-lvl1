from brain_games.cli import welcome_user


_quiz_dict: dict = {}  # Global dictionary, question: answer.
_user_name: str = ""  # Global variable, string with username


def start_quiz_game(quiz_rules: str, quiz_questions: tuple):
    """Controls the flow of the game
    Args:
        quiz_rules (str): String with rules for a current game,
            will be printed for user.
        quiz_questions (tuple(of tuples)): Questions and answers for quiz,
            tuple contains multiple tuples with pairs of strings,
            number of tuples == number of questions, first string becomes
            printed question, second is the correct answer.
    """

    _set_questions_for_quiz(quiz_questions)
    print("Welcome to the Brain Games!")
    _set_user_name()
    print(f"Hello, {_user_name}!")
    print(quiz_rules)
    _play_game()


def _set_questions_for_quiz(questions: tuple):
    global _quiz_dict
    _quiz_dict = {question: answer for question, answer in questions}


def _set_user_name():
    global _user_name
    _user_name = welcome_user()


def _play_game():
    for question, answer in _quiz_dict.items():
        user_input = input(f"Question: {question}\nYour answer: ")
        if user_input == answer:
            print("Correct!")
        else:
            _game_over(user_input, answer)
    else:
        _end_game_player_wins()


def _end_game_player_wins():
    print(f"Congratulations, {_user_name}!")
    quit()


def _game_over(user_input: str, answer: str):
    print(f"{user_input!r} is wrong answer ;(. Correct answer was {answer!r}.")
    print(f"Let's try again, {_user_name}!")
    quit()
