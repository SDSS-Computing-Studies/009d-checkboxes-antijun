#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk
from tkinter import *


def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal

    return decimal
    pass


def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's

    return binary
    pass


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes

    binary = binary_to_decimal(decimal)
    pass


def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    decimal = binary_to_decimal(binary)
    pass


win = tk.Tk()

l1 = Label(win, text="Binary / Decimal Converter!")

cF = Frame()
c1 = Checkbutton(cF)
c2 = Checkbutton(cF)
c3 = Checkbutton(cF)
c4 = Checkbutton(cF)
c5 = Checkbutton(cF)
c6 = Checkbutton(cF)
c7 = Checkbutton(cF)
c8 = Checkbutton(cF)

bF = Frame()
b1 = Button(bF, text="Convert to Binary", command=get_binary)
b2 = Button(bF, text="Convert to Decimal", command=get_decimal)

e1 = Entry(win)

l1.pack()

cF.pack()
c1.pack(side=LEFT)
c2.pack(side=LEFT)
c3.pack(side=LEFT)
c4.pack(side=LEFT)
c5.pack(side=LEFT)
c6.pack(side=LEFT)
c7.pack(side=LEFT)
c8.pack(side=LEFT)

bF.pack()
b1.pack(side=LEFT)
b2.pack(side=LEFT)

e1.pack()


win.mainloop()
