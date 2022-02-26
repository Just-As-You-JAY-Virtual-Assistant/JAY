from curses import window
from tkinter import *
from turtle import title
from neural_path_way import requesting

def start():
    requesting(inputval.get())
    inputval.set("")


window = Tk()
window.title("JAY")

titles = Label(window, text="JAY")
titles.pack()

inputval = StringVar()
inputs = Entry(window, textvariable=inputval)
inputs.pack()

submit = Button(window, text="SUBMIT", command=start)
submit.pack()

window.mainloop()