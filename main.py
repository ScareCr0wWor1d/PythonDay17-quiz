from data import question_data
from question_model import Question
from brain_quiz import QuizzBrain
from random import shuffle
from art import logo

question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

shuffle(question_bank)

new_quizz = QuizzBrain(question_bank)
print(logo)
while new_quizz.q_disp():
    answer = new_quizz.next_question()

print("Thank you for playing!")
