"""Quiz Game

Setup (in a virtual environment):
    pip install cowsay
Run:
    python quiz.py

Topics used: lists, tuples, sets, dictionaries, modules, random, math,
input and casting, if/else, for and while loops, range, booleans and None,
try/except, string formatting.
"""

import math
import random

import cowsay                          # installed with pip
from questions import QUESTIONS       # our own module


def ask_question(number, total, question):
    """Ask one question.

    Returns True (correct), False (wrong) or None (skipped / no answer).
    """
    print(f"\nQuestion {number} of {total}")
    print(question["question"])

    # enumerate numbers the choices 1, 2, 3, 4
    for position, choice in enumerate(question["choices"], start=1):
        print(f"  {position}. {choice}")

    raw = input("Your answer (1-4, or press Enter to skip): ").strip()

    if raw == "":                       # nothing typed
        print("Skipped.")
        return None

    try:
        answer = int(raw)               # casting text to a number
    except ValueError:
        print("That wasn't a number, so it counts as wrong.")
        return False

    if answer == question["answer"]:
        print("Correct!")
        return True

    correct_text = question["choices"][question["answer"] - 1]
    print(f"Wrong. The correct answer was {question['answer']}. {correct_text}")
    return False


def pick_questions(how_many):
    """Pick random questions, using a set so none repeats."""
    asked = set()                       # indexes already chosen
    while len(asked) < how_many:
        index = random.randrange(len(QUESTIONS))
        if index in asked:              # already used, try again
            continue
        asked.add(index)
    return [QUESTIONS[i] for i in asked]


def ask_how_many():
    """Ask how many questions to play, with validation."""
    maximum = len(QUESTIONS)
    while True:
        raw = input(f"How many questions? (1-{maximum}, default 5): ").strip()
        if raw == "":
            return min(5, maximum)
        try:
            count = int(raw)
        except ValueError:
            print("Please type a number.")
            continue
        if 1 <= count <= maximum:
            return count
        print(f"Please choose between 1 and {maximum}.")


def grade_message(percentage):
    """Return feedback for the score."""
    if percentage == 100:
        return "Perfect score!"
    elif percentage >= 70:
        return "Great job!"
    elif percentage >= 40:
        return "Not bad, keep practising."
    return "Time to review the basics."


def play_round():
    """Play one full round and show the result."""
    total = ask_how_many()
    questions = pick_questions(total)

    score = 0
    skipped = 0

    for number in range(1, total + 1):          # range for question numbers
        result = ask_question(number, total, questions[number - 1])
        if result is True:
            score += 1
        elif result is None:
            skipped += 1

    percentage = math.floor(score / total * 100)   # math module
    print("\n" + "=" * 30)
    print(f"Score: {score}/{total} ({percentage}%)")
    if skipped:
        print(f"Skipped: {skipped}")
    print(grade_message(percentage))
    print("=" * 30)

    # the cow announces the final score
    cowsay.cow(f"You scored {score} out of {total}!")


def main():
    print("Welcome to the Python Quiz Game!")
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()