from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# ---- Create New Flash Cards
# Pick random word from csv
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def generate_word():
    current_card = random.choice(to_learn)
    front_card.itemconfig(title_text, text="French")
    front_card.itemconfig(word_text, text=current_card["English"])


# ---- UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# front card
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
front_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card.create_image(400, 263, image=front_card_img)
title_text = front_card.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = front_card.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
front_card.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_word)
wrong_btn.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_word)
right_btn.grid(row=1, column=1)

generate_word()

window.mainloop()
