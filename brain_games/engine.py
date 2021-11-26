import brain_games.cli


NUMBER_OF_ROUNDS = 3


def start_game(quiz_rules, quiz_game):
    print("Welcome to the Brain Games!")
    user_name = brain_games.cli.welcome_user()
    print(f"Hello, {user_name}!")
    print(quiz_rules)
    for _ in range(NUMBER_OF_ROUNDS):
        question, answer = quiz_game()
        user_input = input(f"Question: {question}\nYour answer: ")
        if user_input == answer:
            print("Correct!")
        else:
            print(
                f"{user_input!r} is wrong answer ;(. Correct answer was {answer!r}."
            )
            print(f"Let's try again, {user_name}!")
            quit()
    else:
        print(f"Congratulations, {user_name}!")
        quit()
