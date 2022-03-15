import random
from tkinter import *

layout = Tk()

layout.geometry("500x500")
layout.title("Dark Shadow")
label1 = Label(layout, text="DARK SHADOW", background="#012")
label1.pack(ipadx=700, ipady=700, padx=0, pady=0)

def input ():
    text_box = inputtxt.get(1.0, "end-lc")
add_txt = Text(label1, height=5, width=10)
add_txt.place()

layout.mainloop()
