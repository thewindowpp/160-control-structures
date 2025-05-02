"""
Mission: Quiz/Flashcard App with Scoring

Instructions:
- Complete this Python script to meet the Mission requirements.
- Include at least five questions.
- Track the user's score.
- Give feedback after each question.
- Show the final score.
- Allow replaying or exiting.
"""

def main():
    print("Welcome to the Quiz App!")
    score = 0

    # Example question list (you can expand or modify)
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 5 + 7?", "answer": "12"},
        {"question": "What programming language is this app written in?", "answer": "Python"},
        {"question": "What loop checks a condition before running?", "answer": "while"},
        {"question": "What keyword exits a loop early?", "answer": "break"}
    ]

    play_quiz = True
    while play_quiz:
        score = 0
        for q in questions:
            user_answer = input(q["question"] + " ")
            if user_answer.strip().lower() == q["answer"].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {q['answer']}.")
        print(f"\nYour final score is {score} out of {len(questions)}.")

        replay = input("Do you want to play again? (yes/no) ")
        if replay.strip().lower() != "yes":
            play_quiz = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()