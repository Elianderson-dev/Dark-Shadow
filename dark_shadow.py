import random
import tkinter

layout = tkinter.Tk()

layout.title("Dark Shadow")
layout.geometry("500x500")
layout.configure(background="#001")

label1 = tkinter.Label(layout, text="DARK SHADOW", background="#012")
label1.pack(ipadx=700, ipady=700, padx=0, pady=0)

add_text = tkinter.Entry(label1)

font_select = ("PermanentMarker Regular", 20)

add_text.configure(font = font_select)
layout.mainloop()
