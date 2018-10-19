from tkinter import *
import datetime

def tijd():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%H")
    s = int(s)
    if s < 12:
        return('Goedemorgen')
    elif s >= 12 and s < 18:
        return('Goedemiddag')
    elif s > 18:
        return('Goedenavond')


root = Tk()

label = Label(master=root,
              text=tijd() + '\n\nWelkom bij NS',
              background='yellow',
              foreground='blue',
              font=('Helvetica', 25, 'bold'),
              width=50,
              height=15)
label.pack()

Doorgaan = Button(master=root, text='Doorgaan', height=3, width=15, font=('Helvetica', 15, 'bold'), background='royalblue',
              foreground='white')
Doorgaan.place(x=407, y=400)

root.mainloop()