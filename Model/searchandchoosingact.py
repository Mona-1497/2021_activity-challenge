from tkinter import *
from PIL import Image,ImageTk
import webbrowser
import os
import sys
root = Tk()
root.title("Searching And choosing Activity")
root['background']='#064134'
root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
photo = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/search.png")
def callback():
    os.system('SearchAct.py')

searchbtn=Button(root,image=photo,padx=100,command=callback)
searchbtn.grid(row=3,column=1)

s0=Label(root,text="             ",bg='#064134')
s0.grid(column=0)
searchlb=Label(root,text='Search For An Activity',font=5,pady=10,bg='#064134',fg='white')
searchlb.grid(row=2,column=1)
s1=Label(root,text="             ",bg='#064134')
s1.grid(column=2)

photo2 = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/random.png")
def callback2():
    os.system('RandomAct.py')
rndhbtn=Button(root,image=photo2,width=225,height=225,padx=100,command=callback2)
rndhbtn.grid(row=3,column=3)
rndlb=Label(root,text='Random Activity',font=5,pady=10,bg='#064134',fg='white')
rndlb.grid(row=2,column=3)
s2=Label(root,text="             ",bg='#064134')
s2.grid(column=3)

s3=Label(root,text="             ",bg='#064134')
s3.grid(column=4)
photo3 = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/shared.png")
def callback3():
    os.system('SharedAct.py')
sharedbtn=Button(root,image=photo3,width=225,height=225,padx=100,command=callback3)
sharedbtn.grid(row=3,column=5)
shlb=Label(root,text='Shared Activity',font=5,pady=10,bg='#064134',fg='white')
shlb.grid(row=2,column=5)

l=Label(root,text='    ',bg="#064134")
l.grid(row=4,column=3)

l2=Label(root,text='    ',bg="#064134")
l2.grid(row=5,column=3)

l3=Label(root,text='    ',bg="#064134")
l3.grid(row=6,column=3)
photo4=PhotoImage(file="C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/back.png")
def callback4():
    os.system('MainMenu.py')
backbtn=Button(root,image=photo4,command=callback4,borderwidth=0)
backbtn.grid(row=7,column=3)
root.mainloop()