from tkinter import *
import pandas
import random

BACKGROUND_COLOR="#B1DDC6"
current_card={}
to_learn={}

try:
    data=pandas.read_csv(r"C:\Users\tambe\OneDrive\Desktop\Python\Flash_Card_Project\data\word_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv(r"C:\Users\tambe\OneDrive\Desktop\Python\Flash_Card_Project\data\Hindi-English.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    global current_card,fliptimer
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="Hindi",fill="black")
    canvas.itemconfig(card_word,text=current_card["Hindi"],fill="black")
    canvas.itemconfig(card_background,image=card_Front_img)
    fliptimer=window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv(r"C:\Users\tambe\OneDrive\Desktop\Python\Flash_Card_Project\data\word_to_learn.csv",index=False)
    next_card()


    

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
fliptimer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_Front_img=PhotoImage(file=r"C:\Users\tambe\OneDrive\Desktop\Python\Flash_Card_Project\image\card_front.png")
card_back_img=PhotoImage(file=r"C:\Users\tambe\OneDrive\Desktop\Python\Flash_Card_Project\image\card_back.png")
card_background=canvas.create_image(400,263,image=card_Front_img)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file=r"C:\Users\tambe\OneDrive\Desktop\Python\Flash_Card_Project\image\wrong.png")
unknown_button=Button(image=cross_image,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file=r"C:\Users\tambe\OneDrive\Desktop\Python\Flash_Card_Project\image\right.png")
known_button=Button(image=check_image,command=is_known)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()