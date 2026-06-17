questions = [
    ("What is the capital of France?", "paris"),
    ("How many planets are in our solar system?", "8"),
    ("Which element has the chemical symbol 'O'?", "oxygen"),
]

score = 0
for question, answer in questions:
    if input(question + " ").strip().lower() == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer: {answer}")

print(f"\nFinal score: {score}/{len(questions)}")
