#
#

import random as rnd

from lecture_1.oop.basic_oop.quiz_app import question as qn


class Quiz:
    def __init__(self, questions_):
        self.questions = rnd.sample(questions_, len(questions_))
        self.question_index = 0
        self.score = 0

    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = self.get_question()
        print(f"Question_{self.question_index + 1}: \n\n{question.text}")
        print(f"\n"
              f"A: {question.choices[0]}     \nB: {question.choices[1]}\n"
              f"C: {question.choices[2]}     \nD: {question.choices[3]}")

        answer = input("Choice: ")
        if question.check_answer(answer):
            self.score += 1

    def load_question(self):

        while self.question_index < len(self.questions):
            self.display_progress()
            self.display_question()
            if self.question_index == len(self.questions) - 1:
                self.display_score()
                break
            self.question_index += 1

    def display_score(self):
        print("Score:", self.score)

    def display_progress(self):
        total_question = len(self.questions)
        current_qusstion = self.question_index + 1

        print(f"Total question count: {total_question}, your question number: {current_qusstion}".center(60, "*"))


q1 = qn.Question("What is the popular programming language of 2021?", ["Python", "Java", "C#", "Go"], "Python")

q2 = qn.Question("What is the oldest programming language?", ["Python", "Java", "C", "C++"], "C")

q3 = qn.Question("Which language is supported by Google?", ["Python", "Java", "C#", "Go"], "Go")

questions = [q1, q2, q3]

quiz = Quiz(questions)

quiz.load_question()
