#
#
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer_):
        if answer_ not in self.choices:
            raise ValueError("Answer not in choices")
        return self.answer == answer_
