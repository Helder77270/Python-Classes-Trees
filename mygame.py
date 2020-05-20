from tkinter import *
from PIL import *

WIDTH = 300
HEIGHT = 300

fen1 = Tk()
fen1.title("Push your git !")

photolabel = Label(fen1,text = "HI" )
namefield = Entry(fen1, justify = CENTER, relief="solid", borderwidth = 2)
btnjouer = Button(fen1, text ='Jouer', anchor = SW)
photo = PhotoImage(file='download.png')
label = Label(fen1, image = photo, width = WIDTH, height = HEIGHT)

label.pack()
photolabel.pack()
namefield.pack()
btnjouer.pack()

fen1.mainloop()


