import prompt


def welcome_user() -> str:
    """Returns string with user input (name)"""
    return prompt.string("May I have your name? ")
