from tkinter import * 
import random

root = Tk()
root.title("RPS")
width = 600
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y= (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height , x, y))
root.resizable(0,0)
root.config(bg="purple")


player_earth = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/earth-user.png').subsample(2)
player_fire = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/fire-user.png').subsample(2)
player_water = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/water-user.png').subsample(2)
player_metal = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/metal-user.png').subsample(10)
player_wood = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/wood-user.png').subsample(2)
comp_metal = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/metal-comp.png').subsample(10)
comp_fire = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/fire-comp.png').subsample(2)
comp_wood = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/wood-comp.png').subsample(2)
comp_water = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/water-comp.png').subsample(2)
comp_earth = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/earth-comp.png').subsample(2)
start = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/draw.png').subsample(4)
draw = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/draw.png').subsample(4)
win = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/win.png').subsample(4)
lose = PhotoImage(file='C:/Users/ASUS/Desktop/Letsgo/lose.png').subsample(4)

player_img = Label(root, image=player_earth, bg="purple")
player_img.grid(row=2 , column = 1 , padx=30 , pady=30)
comp_img = Label(root, image=comp_earth , bg="purple")
comp_img.grid(row=2 , column =3 , padx=40 , pady=40)

lbl_player = Label(root, font=("Arial", 15), text='Player', bg ='purple', fg ='white')
lbl_player.grid(row = 1 , column = 1)
lbl_comp = Label(root, font=("Arial", 15), text='Comp', bg ='purple', fg ='white')
lbl_comp.grid(row = 1 , column = 3)

player_score = Label(root , font=("Arial", 15), text='0', bg ='purple', fg ='white')
breaklbl = Label(root , font=("Arial", 15), text='-', bg ='purple', fg ='white')
comp_score = Label(root , font=("Arial", 15), text='0', bg ='purple', fg ='white')
player_score.grid(row=3 , column=1)
breaklbl.grid(row=3 , column = 3)
comp_score.grid(row=3 , column=3)
msg = Label(root , font=("Arial", 15), bg ='purple', fg ='white')
msg.grid(row=2 , column=2)
msg.configure(image=start)

def updatePlayerScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = score

def updateCompScore():
    score = int(comp_score['text'])
    score +=1
    comp_score['text'] = score

def earth():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_earth)
    MatchProcess()

def fire():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_fire)
    MatchProcess()

def water():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_water)
    MatchProcess()

def metal():
    global player_choice
    player_choice = 4
    player_img.configure(image=player_metal)
    MatchProcess()

def wood():
    global player_choice
    player_choice = 5
    player_img.configure(image=player_wood)
    MatchProcess()

def MatchProcess():
    comp_choice = random.randint(1, 5)
    if comp_choice ==1:
        comp_img.configure(image=comp_earth)
        Computerearth()
    elif comp_choice ==2:
        comp_img.configure(image=comp_fire)
        Computerfire()
    elif comp_choice ==3:
        comp_img.configure(image=comp_water)
        Computerwater()
    elif comp_choice ==4:
        comp_img.configure(image=comp_metal)
        Computermetal()
    else:
        comp_img.configure(image=comp_wood)
        Computerwood()

def Computerearth():
    if player_choice == 1:
        msg.configure(image=draw)
    elif player_choice ==2:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice ==3:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice ==4:
        msg.configure(image=win)
        updatePlayerScore()
    else:
        msg.configure(image=lose)
        updateCompScore()

def Computerfire():
    if player_choice == 1:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice ==2:
        msg.configure(image=draw)
    elif player_choice ==3:
        msg.configure(image=draw)
    elif player_choice == 4:
        msg.configure(image=win)
        updatePlayerScore()
    else:
        msg.configure(image=lose)
        updateCompScore()

def Computerwater():
    if player_choice == 1:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image=draw)
    elif player_choice ==3:
        msg.configure(image=draw)
    elif player_choice ==4:
        msg.configure(image=win)
        updatePlayerScore()
    else: 
        msg.configure(image=lose)
        updateCompScore()

def Computermetal():
    if player_choice == 1:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice ==2:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice == 3:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice ==4:
        msg.configure(image=draw)
    else: 
        msg.configure(image=lose)
        updateCompScore()

def Computerwood():
    if player_choice == 1:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice ==3:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice ==4:
        msg.configure(image=win)
        updatePlayerScore()
    else: 
        msg.configure(image=draw)
        
def ExitApp():
    root.destroy()
    exit()

sm_player_earth= player_earth.subsample(1,1)
sm_player_metal= player_metal.subsample(1,1)
sm_comp_metal= comp_metal.subsample(1,1)
earth = Button(root, image=player_earth, command=earth , bg="purple")
earth.grid(row = 4, column = 1)
fire = Button(root, image=player_fire, command=fire , bg="purple")
fire.grid(row = 4 , column = 2)
water = Button(root, image=player_water, command=water , bg="purple")
water.grid(row = 4 , column = 3)
wood = Button(root, image=player_wood, command=wood , bg="purple")
wood.grid(row = 4 , column = 4)
metal = Button(root, image=player_metal, command=metal , bg="purple")
metal.grid(row = 4 , column = 7)
exit = Button(root, text="exit" ,command=exit , bg="red")
exit.grid(row = 1 , column = 5)
Start = Button(root ,)
root.mainloop()