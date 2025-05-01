# Mission Instructions: Quiz/Flashcard App

This project is part of the 1.65 Mission task for Stage 6 Software Engineering.

## Project Overview

You will develop a **quiz or flashcard app** in Python that:
- Asks the user at least five predefined questions
- Checks their answers and gives immediate feedback
- Tracks the score
- Displays the final result at the end
- Offers the option to replay or quit

## Requirements

- Use loops, selection, and sequence structures
- Write clear, commented Python code
- Provide pseudocode or flowchart planning as part of your submission (optional, can be included in your repo)
- Save your work in a `.py` file, not a notebook

### Optional Extensions

- Randomise question order
- Load questions from an external text file
- Allow users to add their own questions
- Keep a score history across sessions

## How to Run

1. Open the `mission-quiz-app.py` file in your Python IDE or editor.
2. Run the script.
3. Follow the on-screen instructions.

## Code Comprehension Questions

In addition to completing and running the quiz app, you are expected to **read the provided scaffold carefully** and add comments in the `.py` file to answer the following questions.

Add your answers as inline comments (using `#`) near the relevant line in the code.

1. What is the purpose of the `main()` function, and why is the main program logic placed inside it?

2. What does the line `if __name__ == "__main__": main()` do, and why is it included?

3. What Python data type is the `questions` variable, and how is it structured?

4. How does the `for q in questions:` loop work, and what does `q` represent?

5. Why do we use `user_answer.strip().lower()` when checking the user's input?

6. What is the purpose of the `score` variable, and where is it reset?

7. How does the `while play_quiz:` loop control the flow of the entire quiz?

8. What would happen if the user enters an invalid option when asked if they want to play again?

9. What is the purpose of the `break` statement, and where could it be used in this program?

10. If you wanted to extend this app to load questions from a file, where in the code would you make changes?

## Submission

- Commit your `.py` file and any optional files (e.g., `questions.txt`) to your personal GitHub repository.
- Include a short written reflection in a `reflection.md` or as comments in your code:
  - What worked well?
  - What was challenging?
  - How did you test your app?
  - What improvements would you make?
