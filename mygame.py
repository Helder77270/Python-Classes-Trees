from tkinter import *

fen1 = Tk()
fen1.title("Push your git !")

photolabel = Label(fen1,text = "HI" )
namefield = Entry(fen1, justify = CENTER, relief="solid", borderwidth = 2)
btnjouer = Button(fen1, text ='Jouer', anchor = SW)



namefield.pack()
btnjouer.pack()
photolabel.pack()
fen1.mainloop()