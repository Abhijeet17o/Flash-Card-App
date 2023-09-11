import tkinter
import time
import random 
import data_french

BACKGROUND_COLOR = "#B1DDC6"
# WORD = list(data_french.DATA[random.randint(0, len(data_french.DATA))].keys())
# Card size = 800x526

WORD_ENG = {}

def on_click_change():
    global flip_timer
    key, value = random_word()
    WORD_ENG["English"] = value
    
    window.after_cancel(flip_timer)
    canvas_obj.itemconfig(canvas_img, image=card_front)
    canvas_obj.itemconfig(canvas_lang_txt, text="French", font=("Arial", 40, "italic"), fill="black")
    canvas_obj.itemconfig(canvas_word, text=key, font=("Arial", 60, "bold"), fill="black") 
    flip_timer = window.after(3000, func=change_card)
    # change_timer()

# def change_timer():
#     global flip_timer
#     flip_timer = window.after(3000, func=change_card)

def change_card():
    canvas_obj.itemconfig(canvas_img, image=card_back)                                                          #Change image
    canvas_obj.itemconfig(canvas_word, text=WORD_ENG["English"], font=("Arial", 60, "bold"), fill="white")          #Change word
    canvas_obj.itemconfig(canvas_lang_txt, text="English", font=("Arial", 40, "italic"), fill="white")          #Change language

def random_word() -> str:
    DICT = data_french.DATA[random.randint(0, len(data_french.DATA))] 
    KEY = list(DICT.keys())
    VALUE = list (DICT.values())
    return KEY[0], VALUE[0]

#Creating window
window = tkinter.Tk()
window.configure(bg=BACKGROUND_COLOR)
window.title("Flash Card App")
window.minsize(width=800, height=600)

#Creating canvas
canvas_obj = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

#Creating card, right and wrong image object
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
right_image = tkinter.PhotoImage(file="./images/right.png")
wrong_image = tkinter.PhotoImage(file="./images/wrong.png")

#Creating right and wrong button
right_button = tkinter.Button(window, image=right_image, command=on_click_change, highlightthickness=0)
wrong_button = tkinter.Button(window, image=wrong_image, command=on_click_change, highlightthickness=0)

#-------------Display-------------#
# Display the card
canvas_img = canvas_obj.create_image(400,263,image=card_front)
canvas_obj.grid(row=0, column=0, columnspan=2, padx=30, pady=20)

#Creating canvas text object
canvas_lang_txt = canvas_obj.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas_word = canvas_obj.create_text(400, 263, text="", font=("Arial", 60, "bold"))

#First iteration
key, value = random_word()
WORD_ENG["English"] = value
canvas_obj.itemconfig(canvas_img, image=card_front)
canvas_obj.itemconfig(canvas_lang_txt, text="French", font=("Arial", 40, "italic"))
canvas_obj.itemconfig(canvas_word, text=key, font=("Arial", 60, "bold")) 
flip_timer = window.after(3000, func=change_card)

# Display right button
right_button.grid(row=1,column=1, pady=30)

# Display wrong button
wrong_button.grid(row=1,column=0, pady=30)

window.mainloop()