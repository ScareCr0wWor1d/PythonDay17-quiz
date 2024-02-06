from data import question_data
from question_model import Question
from brain_quiz import QuizzBrain
from random import shuffle
from art import logo
import urllib.request, json
from cleanup import Cleanup

question_bank = []
clean = Cleanup()

# https://opentdb.com/
with urllib.request.urlopen("https://opentdb.com/api.php?amount=50&encode=url3986&type=boolean") as url:
    data = json.load(url)

for each in data['results']:
    q = clean.cleanup(each['question'])
    r = each['correct_answer']
    question_bank.append(Question(q, r))

new_quizz = QuizzBrain(question_bank)
print(logo)
while new_quizz.q_disp():
    answer = new_quizz.next_question()

print("Merci d'avoir jouer!")
print(f"Votre pointage final est : {new_quizz.score}/{len(new_quizz.quest)}")
