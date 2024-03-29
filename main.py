BACKGROUND_COLOR = "#B1DDC6"
current_card=''
words_dict = {}
import warnings
warnings.filterwarnings('ignore', '\nPyarrow', DeprecationWarning)
from tkinter import *
import pandas as pd
import random

#read data
try:
    words_data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    words_dict = original_data.to_dict(orient='records')
else:
    words_dict = words_data.to_dict(orient='records')
finally:
    print(f'You still have {len(words_dict)-1} to learn')



# function to change words
def changingCards():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_can, image=card_front)
    current_card = random.choice(words_dict)
    fr_word = current_card['French']
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=fr_word, fill='black')
    print(fr_word)
    flip_timer = window.after(3000, flip_card)


#functin to flip card and show translation
def flip_card():
    global current_card
    en_word = current_card['English']
    canvas.itemconfig(card_can, image=card_back)
    canvas.itemconfig(title, fill='white', text='English')
    canvas.itemconfig(word, fill='white', text=en_word)

#function to remove letter from original data and store it in new file
def is_known():
    words_dict.remove(current_card)
    print(len(words_dict))
    data = pd.DataFrame(words_dict)
    data.to_csv('data/words_to_learn.csv', index=False)
    changingCards()



#------------ SET UP UI ------------------------#
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('My FlashCard Project')
flip_timer = window.after(3000, func=flip_card)

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_can = canvas.create_image(410, 261, image=card_front)
title = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

# buttons

img_right = PhotoImage(file='images/right.png')
img_wrong = PhotoImage(file='images/wrong.png')
btn_right = Button(image=img_right, highlightthickness=0, command=is_known)
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=changingCards)

btn_right.grid(column=1, row=1)
btn_wrong.grid(column=0, row=1)


changingCards()

window.mainloop()