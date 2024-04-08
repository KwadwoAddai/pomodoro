from tkinter import *
import math

#SOME CONSTANTS
PINK = '#e2979c'
RED = '#e7305b'
GREEN = 'green'
YELLOW = '#f7f5dd'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

rep = 0
timer = NONE

#Reset mechanism
def reset():
    #CANCEL TIMER, CHANGE TIMER AND LABEL TEXT AND ALSO THE CHECKMARK
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='TIMER', fg=GREEN)
    check.config(text='')
    #CALL THE REP VARIABLE AND MAKE IT ZERO
    global rep
    rep = 0


#Timer mechanism
def start_timer():
    #CALL THE REP VARIABLE AND INCREASE IT ON EACH CALL
    global rep
    rep += 1
    #CHANGE THE MINUTES INTO SECONDS
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

#WHEN REP RUNS 8 TIMES TAKE A LONG BREK
    if rep % 8 == 0:
        #CALL THE COUNT DOWN FUNCTION AND PASS THE LONG SEC VARIABLE AS ARGUMENT
        count_down(long_sec)
        title_label.config(text='BREAK', fg=RED)
        check.config(text='✔', fg=RED)
#ON EACH REP AFTER WORK TAKE A SHORT BREAK
    elif rep % 2 == 0:
        #CALL THE COUNT DOWN FUNCTION AND PASS THE SHORT SEC VARIABLE AS ARGUMENT
        count_down(short_sec)
        title_label.config(text='BREAK', fg=PINK)
        check.config(text='✔', fg=PINK)
    else:
        #CALL THE COUNT DOWN FUNCTION AND PASS THE WORK SEC VARIABLE AS ARGUMENT
        count_down(work_sec)
        title_label.config(text='WORK', fg=GREEN)
        check.config(text='', fg=PINK)

#Count mechanism
def count_down(count):
    #THE COUNT DOWN FUCNTION TAKES AN ARGUMENT FINDS CONVERTS IT INTO MINUTES AND SECONDS
    count_min = math.floor(count/60)
    count_sec = count % 60
    #WHEN SECONDS IS LESS THAN TEN MAKE THE SECOND DOUBLE DIGITS
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    #CALL THE FUNCTION TO CHANGE THE TIMER TEXT IN THE CANVAS
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #WHEN COUNT IS GREATER THAN ZERO
    if count > 0:
        global timer
        #CALL THE AFTER FUNCTION AFTER EACH SECOND IT CALLS THE COUNT DOWN FUNCTION AND BEGINS COUNTDOWN
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

#APPLICATION UI
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

title_label = Label(text='TIMER', font=('Arial', 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=400, height=400, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='pomodoro.png')
canvas.create_image(200, 200, image=img)
timer_text = canvas.create_text(200, 200, text='00:00', fill='white', font=('Arial', 50, 'bold'))
canvas.grid(column=1, row=1)


start_button = Button(text='Start', font=('Arial', 12), fg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text='Reset', font=('Arial', 12), fg=GREEN, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=3)

check = Label(fg=GREEN, bg=YELLOW, font=('Arial', 30), highlightthickness=0)
check.grid(column=1, row=4)

window.mainloop()

