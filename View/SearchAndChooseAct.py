from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import os


root = Tk()
root.title("Searching And choosing Activity")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1920x1080")
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/ser.png"))
resized_image = img.resize((250, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
Label(root,text="choose activity!",font=("Comic Sans MS", 30),bg= '#064134',fg='orange').place(x=450,y=15)


def callback():

      root.destroy()
      os.system('SearchAct.py')


searchBtn = Button(root, image=photo, padx=100, command=callback,bg='#064134',bd=0)
searchBtn.place(x=150,y=240)
searchLb = Label(root, text='Search Activity', font=("Comic Sans MS", 15),  bg='#064134', fg='orange')
searchLb.place(x=200,y=200)


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/rand.png"))
resized_image = img.resize((250, 250), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized_image)

def callback2():
    root.destroy()
    os.system('RandomAct.py')


rndBtn = Button(root, image=photo5, command=callback2,bg='#064134',bd=0)
rndBtn.place(x=500,y=240)
rndLb = Label(root, text='Random Activity', font=("Comic Sans MS", 15), bg='#064134', fg='orange')
rndLb.place(x=550,y=200)


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/shared.png"))
resized_image = img.resize((250, 250), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(resized_image)

def callback3():
    root.destroy()
    os.system('SharedAct.py')


sharedBtn = Button(root, image=photo2, command=callback3,bg='#064134',bd=0)
sharedBtn.place(x=850,y=240)
shLb = Label(root, text='Shared Activity', font=("Comic Sans MS", 15), bg='#064134', fg='orange')
shLb.place(x=900,y=200)


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo4=ImageTk.PhotoImage(resized_image)

def callback4():
    root.destroy()
    os.system('options.py')


backBtn = Button(root, image=photo4, command=callback4, borderwidth=0,bd=0,bg='#064134')
backBtn.place(x=20,y=580)


def callbackhome():
    root.destroy()
    os.system('MainMenu.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
home = ImageTk.PhotoImage(resized_image)
homebtn = Button(root, image=home, command=callbackhome, borderwidth=0, bg='#064134')
homebtn.place(x=20, y=8)
root.mainloop()
