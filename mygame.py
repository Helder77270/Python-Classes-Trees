from tkinter import *
from PIL import *

WIDTH = 300
HEIGHT = 300
MIN_SCORE = 0
MAX_SCORE = 3

fen1 = Tk()
fen1.title("Push your git !")
fen1.maxsize(width=500,height=300)
fen1.minsize(width=500,height=300)
fen1.resizable(width="NO",height="NO")

Frame1 = Frame(fen1)
Frame2 = Frame(fen1)
username = StringVar()
username.set("")

def startGame(x,y):
    geo= str(x) + "x" + str(y)
    F1 = Frame(fen1)
    F1 = Toplevel()
    F1.geometry(geo)

    Button(F1,text="Quit",command=F1.destroy).pack()

def getScoresFromFile():
    file = open("score.txt",'r')
    line = file.readlines()
    sortedScores = []
    i=0
    for lines in line:
        sortedScores.append(line[i].split(","))
        sortedScores[i][1] = int(sortedScores[i][1])
        i = i+1
    sortedScores = sorted(sortedScores, key= lambda score: score[1])

    i=0

    print(sortedScores)
    for i in range(MIN_SCORE,MAX_SCORE):
        j = i+1
        Label(Frame2,text="TOP "+ str(j) + " - "+sortedScores[i][0] + " : "+ str(sortedScores[i][1])).pack()
    #for i in reversed(sortedScores):
    #     j = i+1
    #     Label(Frame2,text="TOP "+ str(j) + " - "+sortedScores[i][0] + " : "+ str(sortedScores[i][1])).pack()


label = Label(Frame2,text = "Score")
namefield = Entry(Frame2, justify = CENTER, relief="solid", borderwidth = 2)
btnjouer = Button(Frame2, text ='Jouer', command=lambda : startGame(600,400))
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


