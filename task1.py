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
    print(binary)
    bn = binary[0] + binary[1] + binary[2] + binary[3] + \
        binary[4] + binary[5] + binary[6] + binary[7]
    decimal = int(bn, 2)
    return decimal


def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's

    a = bin(decimal).replace("0b", "")

    binary = [a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]]

    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = int(e1.get())

    binary = decimal_to_binary(decimal)

    s1.set(binary[0])
    s2.set(binary[1])
    s3.set(binary[2])
    s4.set(binary[3])
    s5.set(binary[4])
    s6.set(binary[5])
    s7.set(binary[6])
    s8.set(binary[7])


def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    b1 = str(s1.get())
    b2 = str(s2.get())
    b3 = str(s3.get())
    b4 = str(s4.get())
    b5 = str(s5.get())
    b6 = str(s6.get())
    b7 = str(s7.get())
    b8 = str(s8.get())

    binary = [b1, b2, b3, b4, b5, b6, b7, b8]
    decimal = binary_to_decimal(binary)

    ebox.set(decimal)


win = tk.Tk()

s1 = IntVar()
s2 = IntVar()
s3 = IntVar()
s4 = IntVar()
s5 = IntVar()
s6 = IntVar()
s7 = IntVar()
s8 = IntVar()

ebox = StringVar()
ebox.set("")

l1 = Label(win, text="Binary / Decimal Converter!")

cF = Frame()
c1 = Checkbutton(cF, onvalue=1, offvalue=0, variable=s1)
c2 = Checkbutton(cF, onvalue=1, offvalue=0, variable=s2)
c3 = Checkbutton(cF, onvalue=1, offvalue=0, variable=s3)
c4 = Checkbutton(cF, onvalue=1, offvalue=0, variable=s4)
c5 = Checkbutton(cF, onvalue=1, offvalue=0, variable=s5)
c6 = Checkbutton(cF, onvalue=1, offvalue=0, variable=s6)
c7 = Checkbutton(cF, onvalue=1, offvalue=0, variable=s7)
c8 = Checkbutton(cF, onvalue=1, offvalue=0, variable=s8)

bF = Frame()
b1 = Button(bF, text="Convert to Binary", command=get_binary)
b2 = Button(bF, text="Convert to Decimal", command=get_decimal)

e1 = Entry(win, textvariable=ebox)

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


b = 200
a = bin(b).replace("0b", "")
print(a)
print(a[0])
print(a[1])
print(a[2])
