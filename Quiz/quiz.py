questions = [
    {
        "question": "Which of these is not a data type in Python?",
        "options": ["Strings", "Integar", "Float", "Biscuit"],
        "answer": "Biscuit"
     },
     {
         "question": "Which data type store numbers with decimal point?",
         "options": ["Float", "Integar", "Strings", "Cat"],
         "answer": "Float"
     }
]

letters = ["A", "B", "C", "D"]

score = 0
for question in questions:
    print(f"Question: {question['question']}")
    for letter, options in zip(letters, question["options"]):
        print(f"{letter}. {options}")
    user_answer = ""
    while not (user_answer in letters):
        user_answer = input("Choose your answer (A - D): ").strip().upper()
        if user_answer not in letters:
            print("Invalid input. Try again")
    
    selected_index = letters.index(user_answer)
    selected_answer = question["options"][selected_index]
    if selected_answer == question["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        
print("Quiz Complete!")
print(f"{score}/{len(questions)}")
