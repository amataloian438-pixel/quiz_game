"""Question bank for the quiz game.

Topics used: lists, tuples, dictionaries.
  - QUESTIONS is a LIST
  - each question is a DICTIONARY
  - the answer choices are a TUPLE (fixed, cannot be changed)
  - "answer" is the number (1 to 4) of the correct choice
"""

QUESTIONS = [
    {
        "question": "Which function prints text to the screen?",
        "choices": ("echo()", "print()", "show()", "display()"),
        "answer": 2,
    },
    {
        "question": "Which of these is a mutable data type?",
        "choices": ("tuple", "string", "list", "int"),
        "answer": 3,
    },
    {
        "question": "What does len([4, 8, 15]) return?",
        "choices": ("2", "3", "4", "15"),
        "answer": 2,
    },
    {
        "question": "Which keyword starts a function definition?",
        "choices": ("func", "define", "function", "def"),
        "answer": 4,
    },
    {
        "question": "What is the result of 7 // 2 ?",
        "choices": ("3.5", "3", "4", "2"),
        "answer": 2,
    },
    {
        "question": "Which data type stores only unique items?",
        "choices": ("list", "tuple", "set", "dictionary"),
        "answer": 3,
    },
    {
        "question": "Which command installs a package from PyPI?",
        "choices": ("pip install", "python get", "venv add", "npm install"),
        "answer": 1,
    },
    {
        "question": "What does int('42') do?",
        "choices": ("Prints 42", "Converts text to a number",
                    "Rounds 42", "Raises an error"),
        "answer": 2,
    },
    {
        "question": "Which loop repeats while a condition is True?",
        "choices": ("for", "while", "repeat", "loop"),
        "answer": 2,
    },
    {
        "question": "What is the value of bool(0) ?",
        "choices": ("True", "None", "False", "0"),
        "answer": 3,
    },
]