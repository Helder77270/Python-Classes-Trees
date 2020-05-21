from tkinter import *
from PIL import *

WIDTH = 300
HEIGHT = 300

fen1 = Tk()
fen1.title("Push your git !")
fen1.maxsize(width=500,height=300)
fen1.minsize(width=500,height=300)
fen1.resizable(width="NO",height="NO")

Frame1 = Frame(fen1)
Frame2 = Frame(fen1)

def getScoresFromFile():
    file = open("score.txt",'r')
    line = "x"
    while line:
        line = file.readlines()
        print(line)
        Label(Frame2,text=line, font="arial")

label = Label(Frame2,text = "Score")
namefield = Entry(Frame2, justify = CENTER, relief="solid", borderwidth = 2)
btnjouer = Button(Frame2, text ='Jouer')
photo = PhotoImage(file='download.png')
labelImg = Label(Frame1, image = photo, width = WIDTH, height = HEIGHT)


Frame1.grid(row=0, column = 0, columnspan= 1,sticky=W)
labelImg.pack()
label.pack(side=TOP)
getScoresFromFile()

Frame2.grid(row=0, column =1, columnspan= 1,sticky=W)
btnjouer.pack(side=LEFT,padx= 10)
namefield.pack(side=RIGHT)

fen1.mainloop()

scores = []


