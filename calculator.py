import tkinter as t
from tkinter import *
window = t.Tk()
window.title("SQI Python Class")
window.resizable(0,0)

# in_path = " "
# menu = Menu()
# window.config(menu=menu)
# window.geometry("50x130")

screen = t.Entry(window, text="0", bd=10, width=60, bg = "black", fg = "white")
screen.grid(row=0, column=0, columnspan=4)

# def say_something(v):
def on_screen(v):
	# screen.insert(0,v) its doubling a single key pressed
	s_length = len(screen.get())
	screen.insert(s_length,v)
	return
def clear_screen():
	screen.delete(0,"end")
	return


	# print ("You are Welcome")
btn_on = t.Button(window, text="ON", font=('arial',20,'bold'), bd=10, width=4, bg = "black", fg="white",).grid(row=1, column=0)
btn_off = t.Button(window, text="OFF", font=('arial',20,'bold'), bd=10, width=4, bg = "black", fg="white",).grid(row=1, column=1)
btn_clear = t.Button(window, text="C",  font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white", command = clear_screen).grid(row=1, column=2)
btn_exponential = t.Button(window, text="E", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen("E")).grid(row=1, column=3)

# btn1 = t.Button(top_frame,text = "Submit", bg = "yellow", fg = "red").pack()
btn7 = t.Button(window, text="7", font=('arial',20,'bold'),  bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen(7))
btn7.grid(row=2, column=0)
btn8 = t.Button(window, text="8", font=('arial',20,'bold'),  bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen(8))
btn8.grid(row=2, column=1)
btn9 = t.Button(window, text="9", font=('arial',20,'bold'),  bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen(9))
btn9.grid(row=2, column=2)
btn_plus = t.Button(window, text="+", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white").grid(row=2, column=3)

btn4 = t.Button(window, text="4", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen(4))
btn4.grid(row=3, column=0)
btn5 = t.Button(window, text="5", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen(5))
btn5.grid(row=3, column=1)
btn6 = t.Button(window, text="6", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen(6))
btn6.grid(row=3, column=2)
btn_minus = t.Button(window, text="-", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white").grid(row=3, column=3)

# btn1 = t.Button(window, text="1", command = say_something).grid(row=3, column=0)
btn1 = t.Button(window, text="1", font=('arial',20,'bold'), bd=10, bg = "black", width = 4, fg = "white", command = lambda: on_screen(1))
btn1.grid(row=4, column=0)
btn2 = t.Button(window, text="2", font=('arial',20,'bold'), bd=10, bg = "black", width = 4, fg = "white", command = lambda: on_screen(2))
btn2.grid(row=4, column=1)
btn3 = t.Button(window, text="3", font=('arial',20,'bold'), bd=10, bg = "black", width = 4, fg = "white", command = lambda: on_screen(3))
btn3.grid(row=4, column=2)
btn_multiply = t.Button(window, text="*", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white").grid(row=4, column=3)

btn_zero = t.Button(window, text="0", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen(0))
btn_zero.grid(row=5, column=0)
btn_point = t.Button(window, text=".", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white", command = lambda: on_screen("."))
btn_point.grid(row=5, column=1)
btn_equal = t.Button(window, text="=", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white").grid(row=5, column=2)
btn_divide = t.Button(window, text="/", font=('arial',20,'bold'), bd=10, width = 4, bg = "black", fg = "white").grid(row=5, column=3)


window.mainloop()


