from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# ---- Create New Flash Cards
# Pick random word from csv
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flash_card.itemconfig(title_text, text="French", fill="black")
    flash_card.itemconfig(word_text, text=current_card["French"], fill="black")
    flash_card.itemconfig(card_background, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flash_card.itemconfig(title_text, text="English", fill="white")
    flash_card.itemconfig(word_text, text=current_card["English"], fill="white")
    flash_card.itemconfig(card_background, image=back_card_img)


# ---- UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# timer
flip_timer = window.after(3000, func=flip_card)

# front card
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = flash_card.create_image(400, 263, image=front_card_img)
title_text = flash_card.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = flash_card.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
flash_card.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_word)
wrong_btn.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_word)
right_btn.grid(row=1, column=1)

generate_word()

window.mainloop()
