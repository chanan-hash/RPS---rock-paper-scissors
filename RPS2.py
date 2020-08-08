from tkinter import *
from tkinter import ttk, messagebox
import random

master = Tk()

master.title ("ROCK PAPER SCISSORS !!")
master.iconbitmap(r'rock_vEL_icon.ico')

TheLabel = Label(master, text = "ROCK PAPER SCISSORS !!" )
TheLabel.grid(row = 0, column = 1)

master.resizable(width=False, height=False)

#global variable
click = True

countWin = 0
countLose = 0
countTie = 0

buttonR = ''
buttonP = ''
buttonS = ''

def play():
    global buttonR,buttonP,buttonS

    buttonR = ttk.Button(text = "Rock", command = lambda: youPick('rock'))
    buttonP = ttk.Button(text = "Paper", command = lambda: youPick('paper'))
    buttonS = ttk.Button(text = "Scissors", command = lambda: youPick('scissors'))

    buttonR.grid(row = 1, column = 0)
    buttonP.grid(row = 1, column = 1)
    buttonS.grid(row = 1, column = 2)

def computerPick():
    choice = random.choice(['rock','paper','scissors'])
    return choice


def youPick(yourChoise):
    global click,countTie,countLose,countWin

    compPick = computerPick()

    if click == True:
        if yourChoise == 'rock':
            if compPick == 'rock':
                countTie +=1
                messagebox.showinfo("mach",f"Computer chose {compPick}, It is a Tie")
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                click = False
            elif compPick == 'paper':
                countLose +=1
                messagebox.showinfo("mach", f"Computer chose {compPick}, You lost, try again ):")
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                click = False
            else:
                countWin +=1
                messagebox.showinfo("mach", f"Computer chose {compPick}, You Won! good for you (:")
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                click = False

        elif yourChoise == 'paper':
            if compPick == 'rock':
                countWin += 1
                messagebox.showinfo("mach", f"Computer chose {compPick}, You Won! good for you (:")
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                click = False
            elif compPick == 'paper':
                countTie += 1
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                messagebox.showinfo("mach", f"Computer chose {compPick}, It is a Tie")
                click = False
            else:
                countLose += 1
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                messagebox.showinfo("mach", f"Computer chose {compPick}, You lost, try again ):")
                click = False

        elif yourChoise == 'scissors':
            if compPick == 'rock':
                countLose += 1
                messagebox.showinfo("mach", f"Computer chose {compPick}, You lost, try again ):")
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                click = False
            elif compPick == 'paper':
                countWin += 1
                messagebox.showinfo("mach", f"Computer chose {compPick}, You Won! good for you (:")
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                click = False
            else:
                countTie += 1
                messagebox.showinfo("mach", f"Computer chose {compPick}, It is a Tie")
                print("win: ", countWin, "Lose: ", countLose, "Tie: ", countTie)
                click = False
    else:
        if yourChoise == 'rock' or yourChoise == 'paper' or yourChoise == 'sciccors':
            click = True



label2 = ttk.Label(master, text = f"Win: {countWin}  Lost: {countLose} Tie: {countTie}")
label2.grid(row = 2, column = 0)


if countWin == 3:
    messagebox.showinfo("mach", "You won the Game!!!")
    exit()

elif countLose == 3:
    messagebox.showinfo("mach", "Game over!")
    quit()


play()
master.mainloop()