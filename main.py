BACKGROUND_COLOR = "#B1DDC6"
TEXT='Trouve'
import warnings
warnings.filterwarnings('ignore', '\nPyarrow', DeprecationWarning)
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
#read data
words_data = pd.read_csv('data/french_words.csv')
words_dict = words_data.to_dict(orient='records')
print(words_dict)

# function to change words
def changingCards():
    current_card = random.choice(words_dict)
    fr_word = current_card['French']
    canvas.itemconfig(title, text='French')
    canvas.itemconfig(word, text=fr_word)
    print(fr_word)

#------------ SET UP UI ------------------------#
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('My FlashCard Project')

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas.create_image(410, 261, image=card_front)
title = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text=TEXT, font=('Arial', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

# buttons

img_right = PhotoImage(file='images/right.png')
img_wrong = PhotoImage(file='images/wrong.png')
btn_right = Button(image=img_right, highlightthickness=0, command=changingCards)
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=changingCards)

btn_right.grid(column=1, row=1)
btn_wrong.grid(column=0, row=1)


changingCards()
window.mainloop()