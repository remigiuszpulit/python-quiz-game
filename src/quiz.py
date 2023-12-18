"""
This is a quiz module.

This module provides a Quiz class that can be used to create a quiz game.
"""

import random
from tkinter import Frame, Button, Label, DISABLED, NORMAL, CENTER

button_args = {
    'text': 'Start',
    'bg': '#8334b4',
    'fg': 'white',
    'font': ('Arial', 16)
}
label_args = {
    'text': 'Welcome to the friends quiz',
    'bg': 'white',
    'font': ('Arial', 18),
    'wraplength': 400
}
common_answer_button_args = {
    'bg': '#8334b4',
    'fg': 'white',
    'font': ('Arial', 16),
    'width': 30,
}

class Quiz():
    """
    This is a Quiz class.

    This class provides methods to manage a quiz game. It keeps track of the score, 
    the current question, and the chosen answer. It also provides methods to start 
    the game, select an answer,  move to the next question, finish and restart the game.
    """
    def __init__(self, questions, length, frame):
        random_index = random.randint(0, len(questions) - 1)
        self.questions = questions
        self.length = length
        self.score = 0
        self.current_question = questions[random_index]
        self.used_questions = [random_index]
        self.chosen_answer = None
        self.answer_frame = Frame(frame, bg='white')
        self.answer_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.is_last_question = False
        self.button = Button(frame, **button_args, command=self.start)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.label = Label(frame, **label_args)
        self.label.place(relx=0.5, rely=0.3, anchor=CENTER)
    def start(self):
        """"
        This method starts the quiz game.
        """
        self.label.config(text=self.current_question['title'])
        self.button.config(text='Next', command=self.next_question, state=DISABLED)
        self.apend_answers()
    def select_answer(self, answer):
        """"
        This method selects an answer and enables the next button.
        """
        self.chosen_answer = answer
        self.button.config(state=NORMAL)
        for widget in self.answer_frame.winfo_children():
            if widget.cget('text') == answer['label']:
                widget.config(bg='#a069c2')
            else:
                widget.config(bg='#8334b4')
    def next_question(self):
        """"
        This method moves to the next question and updates the score if necessary.
        """
        if self.chosen_answer['value'] == 'true':
            self.score += 1
        random_index = random.randint(0, len(self.questions) - 1)
        while random_index in self.used_questions:
            random_index = random.randint(0, len(self.questions) - 1)
        self.chosen_answer = None
        self.current_question = self.questions[random_index]
        self.used_questions.append(random_index)
        self.setis_last_question()
        self.delete_answers()
        self.label.config(text=self.current_question['title'])
        if self.is_last_question:
            self.button.config(text='Finish', command=self.finish)
        else:
            self.button.config(state=DISABLED)
        self.apend_answers()
    def setis_last_question(self):
        """"
        This method sets the is_last_question attribute.
        """
        self.is_last_question = len(self.used_questions) == self.length
    def apend_answers(self):
        """"
        This method appends the answers to the answer frame.
        """
        random.shuffle(self.current_question['answers'])
        for i, answer in enumerate(self.current_question['answers']):
            answer_button_args = {
                'text': answer['label'],
                'command': lambda answer=answer: self.select_answer(answer)
            }
            button = Button(self.answer_frame, **answer_button_args, **common_answer_button_args)
            button.grid(row=i//2, column=i%2, padx=10, pady=10)
    def delete_answers(self):
        """"
        This method deletes the answers from the answer frame.
        """
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
    def finish(self):
        """"
        This method finishes the quiz game and displays the score.
        """
        if self.chosen_answer['value'] == 'true':
            self.score += 1
        self.delete_answers()
        self.label.config(text=f'Your score is {self.score}/{self.length}')
        self.button.config(text='Restart', command=self.restart)
    def restart(self):
        """"
        This method restarts the quiz game.
        """
        self.score = 0
        random_index = random.randint(0, len(self.questions) - 1)
        self.current_question = self.questions[random_index]
        self.used_questions = [random_index]
        self.setis_last_question()
        self.label.config(text=self.current_question['title'])
        self.button.config(text='Next', command=self.next_question, state=DISABLED)
        self.apend_answers()
