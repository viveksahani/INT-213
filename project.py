import tkinter
from tkinter import *

temp = ""


def press(input):
    global temp
    temp = temp + str(input)
    display.set(temp)


def equalpress():
    try:
        global temp
        total = str(eval(temp))
        display.set(total)
        temp = ""
    except:
        display.set("error occured")
        temp = ""


def clear():
    global temp
    temp = ""
    display.set("")


def delete():
    global temp
    temp = temp[:len(temp) - 1:]
    display.set(temp)


top = tkinter.Tk()
top.configure(background="gray")
top.title("Maths_Help")
top.geometry("250x280")
display = StringVar()
expression_field = tkinter.Entry(top, textvariable=display)
expression_field.grid(columnspan=5)
b1 = tkinter.Button(top, text="1", fg="white", bg="black", command=lambda: press(1), height=2, width=7)
b1.grid(row=4, column=0)
b2 = tkinter.Button(top, text="2", fg="white", bg="black", command=lambda: press(2), height=2, width=7)
b2.grid(row=4, column=1)
b3 = tkinter.Button(top, text="3", fg="white", bg="black", command=lambda: press(3), height=2, width=7)
b3.grid(row=4, column=2)
b4 = tkinter.Button(top, text="4", fg="white", bg="black", command=lambda: press(4), height=2, width=7)
b4.grid(row=3, column=0)
b5 = tkinter.Button(top, text="5", fg="white", bg="black", command=lambda: press(5), height=2, width=7)
b5.grid(row=3, column=1)
b6 = tkinter.Button(top, text="6", fg="white", bg="black", command=lambda: press(6), height=2, width=7)
b6.grid(row=3, column=2)
b7 = tkinter.Button(top, text="7", fg="white", bg="black", command=lambda: press(7), height=2, width=7)
b7.grid(row=2, column=0)
b8 = tkinter.Button(top, text="8", fg="white", bg="black", command=lambda: press(8), height=2, width=7)
b8.grid(row=2, column=1)
b9 = tkinter.Button(top, text="9", fg="white", bg="black", command=lambda: press(9), height=2, width=7)
b9.grid(row=2, column=2)
b0 = tkinter.Button(top, text="0", fg="white", bg="black", command=lambda: press(0), height=2, width=7)
b0.grid(row=5, column=1)
Decimal = tkinter.Button(top, text=".", fg="white", bg="black", command=lambda: press("."), height=2, width=7)
Decimal.grid(row=5, column=2)
equal = tkinter.Button(top, text="=", fg="white", bg="black", command=equalpress, height=2, width=7)
equal.grid(row=5, column=0)
plus = tkinter.Button(top, text="+", fg="white", bg="black", command=lambda: press("+"), height=2, width=7)
plus.grid(row=2, column=3)
minus = tkinter.Button(top, text="-", fg="white", bg="black", command=lambda: press("-"), height=2, width=7)
minus.grid(row=3, column=3)
multiply = tkinter.Button(top, text="*", fg="white", bg="black", command=lambda: press("*"), height=2, width=7)
multiply.grid(row=4, column=3)
divide = tkinter.Button(top, text="/", fg="white", bg="black", command=lambda: press("/"), height=2, width=7)
divide.grid(row=5, column=3)
clear = tkinter.Button(top, text="AC", fg="white", bg="black", command=clear, height=2, width=7)
clear.grid(row=6, column=0)
delete = tkinter.Button(top, text="DEL", fg="white", bg="black", command=delete, height=2, width=7)
delete.grid(row=6, column=1)
b10 = tkinter.Button(top, text="(", fg="white", bg="black", command=lambda: press("("), height=2, width=7)
b10.grid(row=6, column=2)
b11 = tkinter.Button(top, text=")", fg="white", bg="black", command=lambda: press(")"), height=2, width=7)
b11.grid(row=6, column=3)
b12 = tkinter.Button(top, text="^", fg="white", bg="black", command=lambda: press("**"), height=2, width=7)
b12.grid(row=7, column=0)
b13 = tkinter.Button(top, text="π", fg="white", bg="black", command=lambda: press("3.14"), height=2, width=7)
b13.grid(row=7, column=1)
b14 = tkinter.Button(top, text="√x", fg="white", bg="black", command=lambda: press("**0.5"), height=2, width=7)
b14.grid(row=7, column=2)
top.mainloop()
