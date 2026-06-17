[README_quiz.md](https://github.com/user-attachments/files/29040674/README_quiz.md)
# Quiz Script (`quiz.py`)

A simple Python quiz game that asks the player a series of questions, validates their answers, and displays a final score.

## What it does

- Presents a set of predefined quiz questions.
- Accepts user input for each question.
- Compares the response to the correct answer.
- Displays `Correct!` or `Wrong! Answer: <correct answer>` for each question.
- Shows the final score after all questions are answered.

## How to run

1. Open a terminal in the project folder.
2. Run the script with:

```bash
python quiz.py
```

3. Answer each question when prompted.

## Built-in questions

The script currently includes these sample questions:

- What is the capital of France?
- How many planets are in our solar system?
- Which element has the chemical symbol 'O'?

## Notes

- Answers are compared in a case-insensitive way.
- Leading and trailing whitespace is ignored.
- The final score is displayed as `score/total questions`.

## Extending the quiz

To add or change questions, edit the `questions` list in `quiz.py`:

```python
questions = [
    ("Question text", "correct answer"),
    ...
]
```
