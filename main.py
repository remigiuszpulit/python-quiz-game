'''
@summary: Main file for the program. This file is used to start the program.

'''

import tkinter as tk
from src.quiz_logic import QuizLogic
from src.quiz_model import QuizModel
from src.view import View

class Main(tk.Tk):
    """
    This is the main class for the program.
    """
    def __init__(self):
        super().__init__()
        self.title = 'Friends Quiz'
        self.configure(bg='#8334b4')
        self.geometry('1000x900')
        view = View(self)
        model = QuizModel()
        QuizLogic(model, view)

if __name__ == '__main__':
    app = Main()
    app.mainloop()
