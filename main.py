import tkinter
import random 
import pandas


BACKGROUND_COLOR = "#B1DDC6"
#This is the input data
data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")

WORD_ENG = {}

def on_click_change():
    global flip_timer
    key, value = random_word()
    WORD_ENG["English"] = value
    
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_img, image=card_front)
    canvas.itemconfig(canvas_lang_txt, text="French", font=("Arial", 40, "italic"), fill="black")
    canvas.itemconfig(canvas_word, text=key, font=("Arial", 60, "bold"), fill="black") 
    flip_timer = window.after(3000, func=change_card)

def change_card():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(canvas_word, text=WORD_ENG["English"], font=("Arial", 60, "bold"), fill="white")
    canvas.itemconfig(canvas_lang_txt, text="English", font=("Arial", 40, "italic"), fill="white")

def random_word() -> str:
    DICT = to_learn[random.randint(0, len(to_learn))]
    KEY = DICT["French"]
    VALUE = DICT["English"]
    return KEY, VALUE

#Creating window
window = tkinter.Tk()
window.configure(bg=BACKGROUND_COLOR)
window.title("Flash Card App")
window.minsize(width=800, height=600)

#Creating canvas
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

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
canvas_img = canvas.create_image(400,263,image=card_front)
canvas.grid(row=0, column=0, columnspan=2, padx=30, pady=20)

#First iteration
key, value = random_word()
WORD_ENG["English"] = value
print(WORD_ENG["English"])
canvas.itemconfig(canvas_img, image=card_front)

#Creating canvas text object
canvas_lang_txt = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.itemconfig(canvas_lang_txt, text="French", font=("Arial", 40, "italic"))
canvas.itemconfig(canvas_word, text=key, font=("Arial", 60, "bold")) 
flip_timer = window.after(3000, func=change_card)

# Display right button
right_button.grid(row=1,column=1, pady=30)

# Display wrong button
wrong_button.grid(row=1,column=0, pady=30)

window.mainloop()
