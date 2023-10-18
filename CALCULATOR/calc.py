from tkinter import *
win = Tk()
win.title("My Calculator")
win.resizable(False, False)
def button_press(num):
    global exp
    exp= input_text.get()
    exp= str(exp) + str(num)
    input_text.set(exp)
def button_oper(opr):
    global exp
    exp = input_text.get()
    exp= str(exp) + str(opr)
    input_text.set(exp)
    global oper
    oper = opr
def clr_scr():
    global exp
    input_text.set("")
    exp = ""
def equal(event):
    global display
    global oper
    global exp
    exp = input_text.get()
    input_text.set("")
    result = float(eval(exp))
    exp = result
    display.insert(0, result)
    input_text.set(result)
display_frame = LabelFrame(win, text="VISHAL'S CALCULATOR", relief=SUNKEN, padx=2, pady=2)
display_frame.grid(row=0, column=0, columnspan=6, padx=6, pady=6)
input_text = StringVar()
display = Entry(display_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=22, bg="#fff", bd=0, justify=RIGHT)
display.pack(ipady= 20)
button_1 = Button(win, padx=30, pady=30, text="1", bg="Grey", command=lambda: button_press(1))
button_2 = Button(win, padx=30, pady=30, text="2", bg="Grey", command=lambda: button_press(2))
button_3 = Button(win, padx=30, pady=30, text="3", bg="Grey", command=lambda: button_press(3))
button_4 = Button(win, padx=30, pady=30, text="4", bg="Grey", command=lambda: button_press(4))
button_5 = Button(win, padx=30, pady=30, text="5", bg="Grey", command=lambda: button_press(5))
button_6 = Button(win, padx=30, pady=30, text="6", bg="Grey", command=lambda: button_press(6))
button_7 = Button(win, padx=30, pady=30, text="7", bg="Grey", command=lambda: button_press(7))
button_8 = Button(win, padx=30, pady=30, text="8", bg="Grey", command=lambda: button_press(8))
button_9 = Button(win, padx=30, pady=30, text="9", bg="Grey", command=lambda: button_press(9))
button_add = Button(win, padx=30, pady=30, text="+", bg="light pink", command=lambda: button_oper("+"))
button_sub = Button(win, padx=30, pady=30, text="-", bg="Peachpuff3", command=lambda: button_oper("-"))
button_div = Button(win, padx=30, pady=30, text="/", bg="PaleTurquoise3", command=lambda: button_oper("/"))
button_mul = Button(win, padx=30, pady=30, text="*", bg="paleGreen3", command=lambda: button_oper("*"))
button_equal = Button(win, padx=30, pady=30, text="=", bg="sienna1", command=lambda: equal(""))
button_clear = Button(win, padx=30, pady=30, text="C", bg="khaki3", command=clr_scr)
button_dec = Button(win, padx=30, pady=30, text=".", bg="khaki3", command=lambda: button_press("."))
button_zero = Button(win, padx=30, pady=30, text="0", bg="grey", command=lambda: button_press(0))
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_div.grid(row=3, column=3)
button_dec.grid(row=4, column=0)
button_zero.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_mul.grid(row=4, column=3)
button_equal.grid(row=1, column=4, rowspan=4, sticky='nsew')  # Make the last column a complete rectangle

win.bind("<Return>", equal)

win.mainloop()