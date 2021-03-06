from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.title("Main Menu")
root['background'] = '#064134'
root.geometry("1920x1080")
Font= ("Helvetica", 30,"bold")
title = Label(root, text='Activity Challenge', bg='#064134', font=Font, fg='orange')
title.place(x=450,y=40)


def callback():
    root.destroy()
    os.system('options.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/str.png"))
resized_image = img.resize((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
startBtn = Button(root, image=photo, bd=0, command=callback,bg='#064134')
startBtn.place(x=250,y=240)


def callback2():
    root.destroy()
    os.system('createoptions.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/crea.png"))
resized_image = img.resize((300, 300), Image.ANTIALIAS)
createPhoto = ImageTk.PhotoImage(resized_image)
createBtn = Button(root, image=createPhoto, bd=0,command=callback2,bg='#064134')
createBtn.place(x=700,y=240)


def callback3():
    root.destroy()
    os.system('userProfile.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/profile.png"))
resized_image = img.resize((80, 80), Image.ANTIALIAS)
proPhoto = ImageTk.PhotoImage(resized_image)
profileBtn = Button(root, image=proPhoto, padx=100, bd=0,command=callback3,bg='#064134')
profileBtn.place(x=20,y=39)


def callback4():
    root.destroy()
    os.system('groups.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/group.png"))
resized_image = img.resize((78, 78), Image.ANTIALIAS)
groupPhoto = ImageTk.PhotoImage(resized_image)
groupBtn = Button(root, image=groupPhoto, padx=100, bd=0,bg='#064134',command=callback4)
groupBtn.place(x=120,y=40)

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/inst.png"))
resized_image = img.resize((80, 80), Image.ANTIALIAS)
instPhoto = ImageTk.PhotoImage(resized_image)
instBtn = Button(root, image=instPhoto, padx=100, bd=0,bg='#064134')
instBtn.place(x=220,y=40)

root.mainloop()
