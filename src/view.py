"""
This module contains the View class.
"""
from tkinter import CENTER, Button, Label
from tkinter.ttk import Frame, Style
import random


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


class View(Frame):
    """
    This is a View class.    """
    def __init__(self, parent):
        super().__init__(parent)
        style = Style()
        style.configure("TFrame", background="white")
        self.configure(width=800, height=600, style="TFrame")
        self.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.answer_frame = Frame(self, style="TFrame")
        self.answer_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button = Button(self, **button_args,)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.label = Label(self, **label_args)
        self.label.place(relx=0.5, rely=0.3, anchor=CENTER)
    def delete_answers(self):
        """"
        This method deletes the answers from the answer frame.
        """
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
    def apend_answers(self, answers, command):
        """"
        This method appends the answers to the answer frame.
        
        """
        random.shuffle(answers)
        for i, answer in enumerate(answers):
            answer_button_args = {
                'text': answer['label'],
                'command': lambda answer=answer: command(answer)
            }
            button = Button(self.answer_frame, **answer_button_args,  **common_answer_button_args)
            button.grid(row=i//2, column=i%2, padx=10, pady=10)
    def set_button(self, text, command, state):
        """"
        This method sets the text of the button.
        """
        self.button.config(text=text ,command=command, state=state)
    def restart(self):
        """"
        This method restarts the game.
        """
        self.button.config(text='Start')
        self.label.config(text='Welcome to the friends quiz')
        self.delete_answers()
