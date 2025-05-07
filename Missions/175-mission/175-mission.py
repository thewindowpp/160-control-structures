# 175 Mission: Category-based Quiz App

"""
Your mission:
- Build a quiz app that:
    * Lets the user select a category (e.g., general knowledge, maths, science)
    * Asks at least 5 questions per category
    * Tracks and displays the user's score
    * Provides feedback after each question and at the end
    * Offers the option to play again or exit

Instructions:
- Write pseudocode (with BEGIN and END) before starting your code.
- Complete the TODOs below.
- Add comments explaining key sections.
- Test your program carefully.
"""

def load_questions():
    """
    TODO: Return a dictionary of categories,
    each with a list of (question, answer) pairs.
    You can hardcode this or extend to load from a file.
    """
    return {
        "General Knowledge": [
            ("What is the capital of France?", "Paris"),
            ("How many continents are there?", "7"),
            ("What colour do you get when you mix red and white?", "Pink"),
            ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
            ("What gas do plants breathe in?", "Carbon dioxide")
        ],
        "Maths": [
            ("What is 5 + 7?", "12"),
            ("What is the square root of 16?", "4"),
            ("What is 9 x 9?", "81"),
            ("What is 100 divided by 4?", "25"),
            ("What is 15 minus 6?", "9")
        ]
    }

def ask_questions(category, questions):
    """
    TODO: Loop through the questions for the selected category.
    Ask the user each question and track correct answers.
    Return the final score.
    """
    pass

def main():
    """
    TODO: Main program loop.
    - Display available categories.
    - Let the user select a category.
    - Call ask_questions().
    - Display the final score.
    - Ask if the user wants to play again or exit.
    """
    pass

if __name__ == "__main__":
    main()
