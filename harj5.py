from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import winsound
import time
import threading
import random

# todo: threading message ape

# colors #
ISLAND_COLOR = "#f6d7b0"
CONTINENT_COLOR = "#808080"
WATER_COLOR = "#ADD8E6"
MONKEY_COLOR = "#964B00"

# size & positions #
MONKEY_SIZE = 15
MOVE_SPEED = .01
DEATH_RISK = .5
START_POINT_X = 130
START_POINT_Y_E = 300
START_POINT_Y_K = 100

ISLAND_EDGE = 116
ISLAND_Y_BOTTOM = 80
ISLAND_Y_TOP = 320
ISLAND_X_LEFT = 10

CONTINENT_EDGE = 216
CONTINENT_Y_BOTTOM = 0
CONTINENT_Y_TOP = 400
CONTINENT_X_RIGHT = 350

e_monkey_pos = 0
k_monkey_pos = 0

message_in_a_monkey = ["send", "help", "to", "ern", "kern"]
message_monkeys = []
msg_counter = 0
ape_counter_p2 = 0
safe_ape = 0

root = tk.Tk()
root.title("Exercise 5")
root.geometry("700x700")

# Frames for gui #
frame = tk.Frame(root)
frame.grid(row=0, column=0)

canvas_frame = tk.Frame(frame)
canvas_frame.grid(row=1, column=0)

canvas = tk.Canvas(canvas_frame, bg=WATER_COLOR, height=400, width=350)
canvas.grid(row=0, column=0)

button_frame = tk.Frame(frame)
button_frame.grid(row=0, column=0, sticky="n")

function_button_frame = tk.Frame(frame)
function_button_frame.grid(row=2, column=0)


# add five buttons to the top line of the window
label = tk.Label(button_frame, text="")
point_button = []
for i in range(5):
    button_temp = tk.Button(button_frame, text="Points: "+str(i+1), padx=40)
    button_temp.grid(row=0, column=i+1)
    point_button.append(button_temp)


# Functions #
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100, 500)


def create_island(canvas, x1, y1, x2, y2, color):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)


def hide_buttons(widget1, widget2):
    widget1.grid_remove()
    widget2.grid_remove()


def show_buttons(widget1, widget2):
    widget1.grid(row=0, column=1)
    widget2.grid(row=0, column=2)


def create_monkey(start_y):
    monkey = canvas.create_oval(START_POINT_X - MONKEY_SIZE, start_y - MONKEY_SIZE,
                                START_POINT_X - MONKEY_SIZE, start_y - MONKEY_SIZE, fill=MONKEY_COLOR)
    return monkey


def send_monkey_swim(args):
    if args == 1:
        e_monkey = create_monkey(START_POINT_Y_E)
        y = e_monkey
        monkey_pos = 0
        global e_monkey_pos
    elif args == 2:
        k_monkey = create_monkey(START_POINT_Y_K)
        y = k_monkey
        monkey_pos = 0
        global k_monkey_pos

    for _ in range(100):
        monkey_pos += 1
        canvas.move(y, +1, 0)
        root.update()
        time.sleep(MOVE_SPEED)

    if args == 1:
        e_monkey_pos = monkey_pos
    elif args == 2:
        k_monkey_pos = monkey_pos

    if e_monkey_pos == 100 and k_monkey_pos == 100:
        i_suppose_i_have_earned_so_much_points(1)
        hide_buttons(ernesti_move_button, kernesti_move_button)
        show_buttons(msg_ernesti_move_button, msg_kernesti_move_button)


def create_monkey_with_msg(args):
    global msg_counter
    global ape_counter_p2
    if args == 1:
        e_monkey_msg = create_monkey(START_POINT_Y_E)
        msgr = e_monkey_msg
        msgr_pos = 0
    elif args == 2:
        k_monkey_msg = create_monkey(START_POINT_Y_K)
        msgr = k_monkey_msg
        msgr_pos = 0

    if msg_counter == 4:
        msg_counter = 0

    ape_with_message = [msgr, message_in_a_monkey[msg_counter], msgr_pos]
    msg_counter += 1
    ape_counter_p2 += 1

    for _ in range(100):
        ape_with_message[2] += 1
        canvas.move(ape_with_message[0], +1, 0)
        root.update()
        time.sleep(MOVE_SPEED)

    if ape_with_message[2] == 100:
        print(ape_with_message[1])

    if ape_counter_p2 == 5:
        i_suppose_i_have_earned_so_much_points(2)
        hide_buttons(msg_ernesti_move_button, msg_kernesti_move_button)
        show_buttons(death_e_move_button, death_k_move_button)
        ape_counter_p2 = 0


def msg_with_risk(args):
    global msg_counter
    global safe_ape
    global ape_counter_p2
    if args == 1:
        e_monkey = create_monkey(START_POINT_Y_E)
        monkey_pos = 0
        monkey = e_monkey
    elif args == 2:
        k_monkey = create_monkey(START_POINT_Y_K)
        monkey_pos = 0
        monkey = k_monkey

    if msg_counter == 4:
        msg_counter = 0

    ape_with_message = [monkey, message_in_a_monkey[msg_counter], monkey_pos]
    msg_counter += 1
    ape_counter_p2 += 1

    for x in range(100):
        if x == 50:
            if random.uniform(0, 1) <= DEATH_RISK:
                winsound.Beep(440+i*100, 500)
                break
        ape_with_message[2] += 1
        canvas.move(ape_with_message[0], +1, 0)
        root.update()
        time.sleep(MOVE_SPEED)

    if ape_with_message[2] == 100:
        print(ape_with_message[1])
        safe_ape += 1

    if safe_ape == 10:
        i_suppose_i_have_earned_so_much_points(3)


def monkey_thread_e(args):
    th_e = threading.Thread(target=create_monkey_with_msg(args))

    th_e.start()
    th_e.join()


def monkey_thread_k(args):
    th_k = threading.Thread(target=create_monkey_with_msg(args))

    th_k.start()
    th_k.join()


ernesti_move_button = tk.Button(function_button_frame, text="Ernesti monkey swim",
                                command=lambda: send_monkey_swim(1))
kernesti_move_button = tk.Button(function_button_frame, text="Kernesti monkey swim",
                                 command=lambda: send_monkey_swim(2))
msg_ernesti_move_button = tk.Button(function_button_frame, text="Ernesti message w monkey",
                                    command=lambda: monkey_thread_e(1))
msg_kernesti_move_button = tk.Button(function_button_frame, text="Kernesti message w monkey",
                                     command=lambda: monkey_thread_k(2))
death_e_move_button = tk.Button(function_button_frame, text="e monkey maybe dead:O",
                                command=lambda: msg_with_risk(1))
death_k_move_button = tk.Button(function_button_frame, text="k monkey maybe dead:O",
                                command=lambda: msg_with_risk(2))

hide_buttons(msg_ernesti_move_button, msg_kernesti_move_button)
hide_buttons(death_e_move_button, death_k_move_button)
show_buttons(ernesti_move_button, kernesti_move_button)

# Create #
create_island(canvas, ISLAND_X_LEFT, ISLAND_Y_BOTTOM,
              ISLAND_EDGE, ISLAND_Y_TOP, ISLAND_COLOR)
create_island(canvas, CONTINENT_X_RIGHT, CONTINENT_Y_BOTTOM,
              CONTINENT_EDGE, CONTINENT_Y_TOP, CONTINENT_COLOR)


# example ...
# i_suppose_i_have_earned_so_much_points(3)
root.mainloop()
