# Simple Quiz Game

questions = {
    "What is the capital of India?": "Delhi",
    "Which language is used for AI?": "Python",
    "What is 5 + 7?": "12",
    "Who developed C language?": "Dennis Ritchie"
}

score = 0

for q, a in questions.items():
    print("\n" + q)
    ans = input("Answer: ")
    if ans.strip().lower() == a.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {a}")

print(f"\nYour Final Score: {score}/{len(questions)}")
