'''QuizModel class.'''
import json
import random

class QuizModel:
    """QuizModel class."""

    def __init__(self):
        """Initialize QuizModel class.""" 
        with open('data/config.json', 'r', encoding='utf-8' ) as f:
            data = json.load(f)
            self.questions = data['questions']
            self.length = data['length']

        random_index = random.randint(0, len(self.questions) - 1)
        self.current_question = self.questions[random_index]
        self.used_questions = [random_index]
        self.score = 0
        self.is_last_question = False
    def next_question(self, is_correct):
        '''This method sets the next question.'''
        random_index = random.randint(0, len(self.questions) - 1)
        while random_index in self.used_questions:
            random_index = random.randint(0, len(self.questions) - 1)
        self.used_questions.append(random_index)
        self.current_question = self.questions[random_index]
        if is_correct:
            self.score += 1
        self.is_last_question = len(self.used_questions) == self.length
    def restart(self):
        '''This method restarts the quiz.'''
        self.score = 0
        random_index = random.randint(0, len(self.questions) - 1)
        self.current_question = self.questions[random_index]
        self.used_questions = [random_index]
        self.is_last_question = False
        