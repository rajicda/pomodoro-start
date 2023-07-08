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
sets = 0
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global sets
    global timer
    window.after_cancel(timer)
    timer = None
    reps = 0
    sets = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    label_check.config(text="")
    label_set.config(text=f"Sets done: {sets}")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        global reps
        global sets
        start_timer()

        if reps % 8 == 1:
            label_check.config(text="")
            sets += 1
            label_set.config(text=f"Sets done: {sets}")
        elif reps % 2 == 0:
            label_check.config(text=label_check.cget("text") + "✔")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

label_check = Label(font=(FONT_NAME, 35, "italic"), fg=GREEN, bg=YELLOW)
label_check.grid(row=3, column=1)

label_set = Label(text=f"Sets done: {sets}", font=(FONT_NAME, 15, "italic"), fg=GREEN, bg=YELLOW)
label_set.grid(row=4, column=1)

start_button = Button(text="Start", highlightthickness=0, command=lambda: start_timer() if timer is None else None)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
