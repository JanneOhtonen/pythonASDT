import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import winsound
import time

# colors #
ISLAND_COLOR = "#f6d7b0"
WATER_COLOR = "#ADD8E6"

# config #
CANVAS_H = 500
CANVAS_W = 500

root = tk.Tk()
root.title("Exercise 6")
root.geometry("700x700")

# gui frames #
frame = tk.Frame(root)
frame.grid(row=0, column=0)

canvas_frame = tk.Frame(frame)
canvas_frame.grid(row=1, column=0)

canvas = tk.Canvas(canvas_frame, bg=WATER_COLOR,
                   height=CANVAS_H, width=CANVAS_W)
canvas.grid(row=0, column=0)

point_frame = tk.Frame(frame)
point_frame.grid(row=0, column=0, sticky="n")

# add five buttons to the top line of the window
label = tk.Label(point_frame, text="").grid(row=0, column=0)
point_button = []
for i in range(5):
    button_temp = tk.Button(point_frame, text="Points: "+str(i+1), padx=40)
    button_temp.grid(row=0, column=i+1)
    point_button.append(button_temp)


def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100, 500)


def create_swimming_pool(canvas, x1, y1, x2, y2, color):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)


create_swimming_pool(canvas, CANVAS_H*1.3, CANVAS_W*1.5,
                     CANVAS_H/1.3, CANVAS_W/1.5, ISLAND_COLOR)
root.mainloop()
