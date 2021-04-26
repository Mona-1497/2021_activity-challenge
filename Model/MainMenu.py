from tkinter import *
from PIL import Image,ImageTk
import webbrowser
import os
import sys
root = Tk()

root.title("Main Menu")
root['background']='#064134'
root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
title=Label(root,text='       Main Menu',bg='#064134',font=30,fg='white',pady=10)
title.grid(row=0,column=2)
def callback():
    os.system('searchandchoosingact.py')
photo = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/start.png")
startbtn=Button(root,image=photo,padx=100,bd=0,command=callback)
startbtn.grid(row=1,column=1)


createphoto = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/create.png")
createtbtn=Button(root,image=createphoto,padx=100,bd=0)
createtbtn.grid(row=1,column=2)

instphoto = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/inst.png")
instbtn=Button(root,image=instphoto,padx=100,bd=0)
instbtn.grid(row=1,column=3)


prophoto = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/profile.png")
profilebtn=Button(root,image=prophoto,padx=100,bd=0)
profilebtn.grid(row=2,column=1)

groupphoto = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/group.png")
groupbtn=Button(root,image=groupphoto,padx=100,bd=0)
groupbtn.grid(row=2,column=2)

root.mainloop()