from korean_romanizer.romanizer import Romanizer
import random
import tkinter as tk
from tkinter import ttk


def get_hangul_word(file):
    word = random.choice(open(file, 'r', encoding="utf-8").readlines())
    return word


def romanize(hangul_word):
    r = Romanizer(hangul_word)
    return r.romanize()


def is_correct(guess, answer):
    if guess.lower() == answer.lower():
        return True
    else:
        return False


def init_round():

    word = get_hangul_word("words.txt")
    w.delete("1.0", tk.END)
    w.insert(tk.END, word)
    guess_entry.delete(0, tk.END)


def validate():
    answer = romanize(w.get("1.0", "end")).rstrip()
    guess = guess_entry.get()
    # guess = input(f"What is the romanization of {word.rstrip()} ?\n")

    if is_correct(guess, answer):
        w.insert(tk.END, "Correct!")
    else:
        w.insert(tk.END, f"Wrong! The correct answer was {answer}")


def main():
    start_button.destroy()
    enter_btn.grid(column=1, row=2)
    next_btn.grid(column=2, row=2)
    guess_entry.grid(column=0, row=2)
    window.update()
    init_round()


window = tk.Tk()
window.geometry("900x900")

question_frm = ttk.Frame(window, padding=5)
question_frm.grid()
w = tk.Text(question_frm, height=2, font=('Times New Roman', 17, 'bold'))
w.grid(row=0, column=0)

start_button = ttk.Button(question_frm, text="Start", command=main)
start_button.grid(column=0, row=0)

guess_frm = ttk.Frame(window, padding=0)
guess_frm.grid(row=2)

guess_entry = tk.Entry(guess_frm)


enter_btn = ttk.Button(guess_frm, text="Enter", command=validate)

next_btn = ttk.Button(guess_frm, text="Next", command=init_round)


window.mainloop()