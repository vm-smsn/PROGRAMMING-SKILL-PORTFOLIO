# Vince Michael J. Samson | ID:04-24-0147
# Exercise 4: Primitive Quiz
# 9/13/2024

# First to have a quiz we need a list of questions.
# The multiplequestions contains tuples where it acts as question.
# Each tuple contains 2 strings, 1 question and 1 correct answer.
multiplequestions = [
    ("What is the capital of France? ", "Paris"),
    ("What is the capital of the United Kingdom? ", "London"),
    ("What is the capital of Spain? ", "Madrid"),
    ("What is the capital of Italy? ", "Rome"),
    ("What is the capital of Germany? ", "Berlin"),
    ("What is the capital of Austria? ", "Vienna"),
    ("What is the capital of Ukraine? ", "Kyiv"),
    ("What is the capital of Greece? ", "Athens"),
    ("What is the capital of Portugal? ", "Lisbon"),
    ("What is the capital of Sweden? ", "Stockholm"),
]

score = 0
# This is your score counter for the quiz, and it will start at 0 to simulate an actual quiz.
for questions, answer in multiplequestions:
    # In this function of code we tell the system that the answer is within the
    # multiplequestions tuple and that it is after the coma.
    user_answer = input(questions).lower()
    # This function converts the answers into lowercase
    if user_answer == answer.lower():
    # This function accepts lowercase answer by making the actual answer lowercase
        print("You're Correct!!!")
        # It displays if ever the user has go the question correct.
        score += 1
        # This adds a point to your total score depending on how many you get correct.
    else:
        print("Wrong answer ✕. The correct answer is:", answer)
        # It displays if ever the user has typed the wrong answer.
print("Your score is:", score, "out of", len(multiplequestions))
# After answering all of the questions, the system shall display your total score.