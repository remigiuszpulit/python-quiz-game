'''This is the main class for the quiz logic.'''

from tkinter import DISABLED


class QuizLogic:
    '''This is the main class for the quiz logic.'''
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.button.config(command=self.start)
        self.chosen_answer = None
    def start(self):
        '''This method starts the quiz.'''
        self.view.label.config(text=self.model.current_question['title'])
        self.view.button.config(text='Next', command=self.next_question, state=DISABLED)
        self.view.apend_answers(self.model.current_question['answers'], self.select_answer)
    def select_answer(self, answer):
        '''This method selects the answer.'''
        self.chosen_answer = answer
        self.view.button.config(state='normal')
        for widget in self.view.answer_frame.winfo_children():
            if widget.cget('text') == answer['label']:
                widget.config(bg='#a069c2')
            else:
                widget.config(bg='#8334b4')

    def next_question(self):
        '''This method sets the next question.'''
        self.model.next_question(self.chosen_answer['value'] == 'true')
        self.view.delete_answers()
        self.view.label.config(text=self.model.current_question['title'])
        self.view.apend_answers(self.model.current_question['answers'], self.select_answer)

        if self.model.is_last_question:
            self.view.button.config(text='Finish', command=self.finish)
        else:
            self.view.button.config(state=DISABLED)
    def finish(self):
        '''This method finishes the quiz.'''
        self.model.next_question(self.chosen_answer['value'] == 'true')
        self.view.label.config(text=f'Your score is {self.model.score}')
        self.view.delete_answers()
        self.view.button.config(text='Restart', command=self.restart)
    def restart(self):
        '''This method restarts the quiz.'''
        self.model.restart()
        self.view.restart()
        self.view.button.config(command=self.start)
