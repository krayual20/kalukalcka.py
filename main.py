import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("360x360")
window.title("Kalkulacka")

def fun1():
    entry1.insert(tk.END, "1")
def fun2():
    entry1.insert(tk.END, "2")
def fun3():
    entry1.insert(tk.END, "3")
def fun4():
    entry1.insert(tk.END, "4")
def fun5():
    entry1.insert(tk.END, "5")
def fun6():
    entry1.insert(tk.END, "6")
def fun7():
    entry1.insert(tk.END, "7")
def fun8():
    entry1.insert(tk.END, "8")
def fun9():
    entry1.insert(tk.END, "9")
def fun0():
    entry1.insert(tk.END, "0")


entry1 = tk.Entry(
    width=40,
    fg="black",
    bg="white"
)
entry1.grid(row=0, column=0, columnspan=4)

button1 = tk.Button(
    text="1",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun1
)
button1.grid(row=1, column=0)
button2 = tk.Button(
    text="2",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun2
)
button2.grid(row=1, column=1)
button3 = tk.Button(
    text="3",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun3
)
button3.grid(row=1, column=2)
buttonx = tk.Button(
    text="x",
    bg="green",
    fg="black",
    width=10,
    height=5,
)
buttonx.grid(row=1, column=3)
button4 = tk.Button(
    text="4",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun4
)
button4.grid(row=2, column=0)
button5 = tk.Button(
    text="5",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun5
)
button5.grid(row=2, column=1)
button6 = tk.Button(
    text="6",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun6
)
button6.grid(row=2, column=2)
button7 = tk.Button(
    text="7",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun7
)
buttondivis = tk.Button(
    text="/",
    bg="green",
    fg="black",
    width=10,
    height=5,
)
buttondivis.grid(row=2, column=3)
button7.grid(row=3, column=0)
button8 = tk.Button(
    text="8",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun8
)
button8.grid(row=3, column=1)
button9 = tk.Button(
    text="9",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun9
)
button9.grid(row=3, column=2)
buttonmin = tk.Button(
    text="-",
    bg="green",
    fg="black",
    width=10,
    height=5,
)
buttonmin.grid(row=3, column=3)
button0 = tk.Button(
    text="0",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=fun0
)
button0.grid(row=4, column=0)
buttonplus = tk.Button(
    text="+",
    bg="green",
    fg="black",
    width=10,
    height=5,
)
buttonplus.grid(row=4, column=1)
buttonAC = tk.Button(
    text="AC",
    bg="green",
    fg="black",
    width=10,
    height=5,
)
buttonAC.grid(row=4, column=2)
buttoneq = tk.Button(
    text="=",
    bg="green",
    fg="black",
    width=10,
    height=5,
)
buttoneq.grid(row=4, column=3)
window.mainloop()