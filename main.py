import random

BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
from pandas import *
from random import *

def correct():
    canvas.itemconfig(french, text=new_word())

def wrongdef():
    canvas.itemconfig(french, text=new_word())

#picking random words
def new_word():
    data = read_csv("data/french_words.csv")
    dict123 = choice(data.to_dict(orient="records"))
    English_word = dict123["English"]
    french_word = dict123["French"]
    return french_word

#creating image

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
cardf_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=cardf_img)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
french = canvas.create_text(400, 263, text=new_word(), font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)


# creating buttons
wrong = PhotoImage(file="images/wrong.png")
button = Button(image=wrong, highlightthickness=0, command=wrongdef)
button.grid(column=1, row=2)

right = PhotoImage(file="images/right.png")
button2 = Button(image=right, highlightthickness=0, command=correct)
button2.grid(column=2, row=2)

window.mainloop()