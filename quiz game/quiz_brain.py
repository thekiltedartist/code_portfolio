class QuizBrain:

    def __init__(self, question_list):
        self.number = 0
        self.list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.list)

    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        user_answer = input(f"Q. {self.number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score+=1
        else:
            print(f"Incorrect, the answer is {correct_answer}")
        print(f'Current Score: {self.score}/{self.number}')

