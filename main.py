BACKGROUND_COLOR = "#B1DDC6"
TEXT='Trouve'
from tkinter import *
from tkinter import messagebox

#------------ SET UP UI ------------------------#
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('My FlashCard Project')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas.create_image(410, 261, image=card_front)
canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
canvas.create_text(400, 263, text=TEXT, font=('Arial', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

# buttons

img_right = PhotoImage(file='images/right.png')
img_wrong = PhotoImage(file='images/wrong.png')
btn_right = Button(image=img_right, highlightthickness=0)
btn_wrong = Button(image=img_wrong, highlightthickness=0)
btn_right.grid(column=0, row=1)
btn_wrong.grid(column=1, row=1)



window.mainloop()