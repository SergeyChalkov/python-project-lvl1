#!/usr/bin/env python
from brain_games.cli import welcome_user


def print_title():
    print("Welcome to the Brain Games!")


def main():
    print_title()
    user_name = welcome_user()
    print(f"Hello, {user_name}!")


if __name__ == "__main__":
    main()
