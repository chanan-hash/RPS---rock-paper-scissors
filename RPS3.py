from tkinter import *
import random

root = Tk()

# change the icon, the py file and the images must be in the same folder
root.iconbitmap(r'paper_WEU_icon.ico')
root.title("Rock Paper Scissors")

#the size, the user won't be able to resize it
root.resizable(width=False, height=False)

#global variable
click = True


## all the photoes must be png' if not it wonwt work
#bring the hand images
RrockPhoto = PhotoImage(file = "Rrock.png")
RpaperPhoto = PhotoImage(file = "Rpaper.png")
RscissorsPhoto = PhotoImage(file = "Rscissors.png")

#bring the RPS images
rockPhoto = PhotoImage(file = "rock.png")
paperPhoto = PhotoImage(file = "paper.png")
scissorsPhoto = PhotoImage(file = "scissors.jpg")

#bring the Win and Lose images
winPhoto = PhotoImage(file = "Win.jpg")
losePhoto = PhotoImage(file = "Lose.jpg")
tiePhoto = PhotoImage(file = "tie.jpg")
wingamePhoto = PhotoImage(file = "winwin.jpg")
gameoverPhoto = PhotoImage(file = "GameOver.jpg")

#now we have the Photoes on our project

#now we will name our Buttonsns, we will just create now the variable for the Buttons
RrockPhotoButton = ""
RpaperPhotoButton = ""
RscissorsPhotoButton = ""

#the Functions for our game

#first one will be paly - it will have the game in it
def play():
    global RrockPhotoButton,RpaperPhotoButton,RscissorsPhotoButton

    RrockPhotoButton = Button(root, image = RrockPhoto, command = lambda: youPick('rock'))
    RpaperPhotoButton = Button(root, image = RpaperPhoto, command = lambda: youPick('paper'))
    RscissorsPhotoButton = Button(root, image = RscissorsPhoto, command = lambda: youPick('scissors'))

    #palce the Button
    RrockPhotoButton.grid(row = 0, column = 0)
    RpaperPhotoButton.grid(row = 0, column = 1)
    RscissorsPhotoButton.grid(row = 0, column = 2)


#select what the Computer is going to be
def computerPick():
    choice = random.choice(['rock','paper','scissors'])
    return choice

#detemine whick Button you picked, and it is going to figure out who won - that is going to be the longer Fun' of thw two who are going to be Kind of short
# we will bribg the variabel click
# compPick will grab the string from above and store it in compPick
# after every pick, we eant to change every photo to something else' acording to the chosie
def youPick(yourChoise):
    global click

    compPick = computerPick()

    if click == True:
        if yourChoise == 'rock':
            RrockPhotoButton.configure(image = rockPhoto)
            if compPick == 'rock':
                RpaperPhotoButton.configure(image = rockPhoto)
                RscissorsPhotoButton.configure(image = tiePhoto)
                click = False
            elif compPick == 'paper':
                RpaperPhotoButton.configure(image = paperPhoto)
                RscissorsPhotoButton.configure(image = losePhoto)
                click = False
            else:
                RpaperPhotoButton.configure(image = scissorsPhoto)
                RscissorsPhotoButton.configure(image = winPhoto)
                click = False

        elif yourChoise == 'paper':
            RpaperPhotoButton.cofigure(image = paperPhoto)
            if compPick == 'rock':
                RrockPhotoButton.configure(image = rockPhoto)
                RscissorsPhotoButton.configure(image = winPhoto)
                click = False
            elif compPick == 'paper':
                RrockPhotoButton.configure(image = paperPhoto)
                RscissorsPhotoButton.configure(image = tiePhoto)
                click = False
            else:
                RrockPhotoButton.configure(image = scissorsPhoto)
                RscissorsPhotoButton.configure(image = losePhoto)
                click = False

        elif yourChoise =='scissors':
            RscissorsPhotoButton.configure(image = scissorsPhoto)
            if compPick == 'rock':
                RpaperPhotoButton.configure(image = rockPhoto)
                RrockPhotoButton.configure(image = losePhoto)
                click = False
            elif compPick == 'paper':
                RpaperPhotoButton.configure(image = paperPhoto)
                RrockPhotoButton.configure(image = winPhoto)
                click = False
            else:
                RpaperPhotoButton.configure(image = scissorsPhoto)
                RrockPhotoButton.configure(image = tiePhoto)
                click = False

# becaus after every click, it became False it will send it here, and here we will turn click to True, and start the game again, and aranged the photoes from the beginning
    else:
        if yourChoise == 'rock' or yourChoise == 'paper' or yourChoise == 'sciccors':
            RrockPhotoButton.congigure(image = RrockPhoto)
            RpaperPhotoButton.congigure(image = RpaperPhoto)
            RscissorsPhotoButton.congigure(image = RscissorsPhoto)
            click = True

play()
root.mainloop()