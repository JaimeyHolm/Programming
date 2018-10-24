from tkinter import *

def clicked():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = "kwadraat: van {} = {}"
    label["text"] = tekst.format(grondtal, kwadraat)

root = Tk()

label = Label(master=root, text='Hello World', height=2)
label.pack()

button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()