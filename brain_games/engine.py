import brain_games.cli


NUMBER_OF_ROUNDS = 3


def start_game(game):
    print("Welcome to the Brain Games!")
    player = brain_games.cli.welcome_user()
    print(f"Hello, {player}!")
    print(game.GAME_RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        question, answer = game.get_question()
        user_input = input(f"Question: {question}\nYour answer: ")
        if user_input == answer:
            print("Correct!")
        else:
            print(f"{user_input!r} is wrong answer ;(. Correct answer was {answer!r}.")
            print(f"Let's try again, {player}!")
            break
    else:
        print(f"Congratulations, {player}!")
