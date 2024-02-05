class QuizzBrain:
    def __init__(self, lst_q):
        self.start = 0
        self.quest = lst_q
        self.score = 0

    def next_question(self):
        curr_q = self.quest[self.start]
        self.start += 1
        answer = input(f"Q.{self.start} :  {curr_q.question} (true/false) : ")
        self.check_ans(answer, curr_q.reponse)

    def q_disp(self):
        return self.start < len(self.quest)

    def check_ans(self, ans, rep):
        if ans.lower() == rep.lower():
            print("Bonne réponse!")
            self.score += 1
        else:
            print("Mauvaise réponse!")
        print(f"La bonne réponse était : {rep}")
        print(f"Score: {self.score}/{self.start}")