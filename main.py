import random

BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
from pandas import *
from random import *

def correct():
    global current_word, flip_timer
    window.after_cancel(flip_timer)

    data = read_csv("data/wordtolearn.csv")
    data = data.loc[data["French"] != current_word["French"]]
    data.to_csv("data/wordtolearn.csv", index=False)
    current_word = new_word()
    canvas.itemconfig(word, text=current_word["French"], fil="black")
    canvas.itemconfig(img, image=cardf_img)
    canvas.itemconfig(title, text="French", fill="black")
    flip_timer = window.after(3000, updatecanvas)
def wrongdef():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = new_word()
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    canvas.itemconfig(img, image=cardf_img)
    canvas.itemconfig(title, text="French", fill="black")
    flip_timer = window.after(3000, updatecanvas)

#picking random words
def new_word():
    try:
        data = read_csv("data/wordtolearn.csv")
    except FileNotFoundError:
        df = read_csv("data/french_words.csv")
        df.to_csv("data/wordtolearn.csv", index=False)
    finally:
        data = read_csv("data/wordtolearn.csv")
        dict123 = choice(data.to_dict(orient="records"))
    return dict123

def updatecanvas():
    canvas.itemconfig(img, image=cardb_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")


current_word = new_word()

#creating image

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
cardf_img = PhotoImage(file="images/card_front.png")
cardb_img = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=cardf_img)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=current_word["French"], font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

# creating buttons
wrong = PhotoImage(file="images/wrong.png")
button = Button(image=wrong, highlightthickness=0, command=wrongdef)
button.grid(column=1, row=2)

right = PhotoImage(file="images/right.png")
button2 = Button(image=right, highlightthickness=0, command=correct)
button2.grid(column=2, row=2)

flip_timer = window.after(3000, updatecanvas)

window.mainloop()
