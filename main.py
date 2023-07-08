from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    countdown(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


label = Label(text="Timer", font=(FONT_NAME, 50, "italic"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

label_check = Label(text="✔", font=(FONT_NAME, 35, "italic"), fg=GREEN, bg=YELLOW)
label_check.grid(row=3, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
