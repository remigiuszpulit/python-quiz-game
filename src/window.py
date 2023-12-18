"""This module sets up the window and launches an instance of Quiz game."""
from tkinter import Tk, Frame, CENTER
import json
from src.quiz import Quiz

def main():
    """
    This function sets up the window and launches an instance of Quiz game.
    """
    window = Tk()
    window.title("Friends Quiz")
    window.configure(bg='#8334b4')
    window.geometry('1000x900')
    frame = Frame(window, width=800, height=600, bg='white')
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    questions = []
    length = 0

    with open('data/config.json', 'r', encoding='utf-8' ) as f:
        data = json.load(f)
        questions = data['questions']
        length = data['length']

    Quiz(questions, length, frame)

    window.mainloop()
