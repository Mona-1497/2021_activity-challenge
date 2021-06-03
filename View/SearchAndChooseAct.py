from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import os
import sys

root = Tk()
root.title("Searching And choosing Activity")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
photo = PhotoImage(file="../View/Pictures/search.png")


def callback():
    root.destroy()
    os.system('SearchAct.py')


searchBtn = Button(root, image=photo, padx=100, command=callback)
searchBtn.grid(row=3, column=1)

s0 = Label(root, text="             ", bg='#064134')
s0.grid(column=0)
searchLb = Label(root, text='Search For An Activity', font=5, pady=10, bg='#064134', fg='white')
searchLb.grid(row=2, column=1)
s1 = Label(root, text="             ", bg='#064134')
s1.grid(column=2)

photo2 = PhotoImage(file="../View/Pictures/play.png")


def callback2():
    root.destroy()
    os.system('RandomAct.py')


rndBtn = Button(root, image=photo2, width=225, height=225, padx=100, command=callback2)
rndBtn.grid(row=3, column=3)
rndLb = Label(root, text='Random Activity', font=5, pady=10, bg='#064134', fg='white')
rndLb.grid(row=2, column=3)
s2 = Label(root, text="             ", bg='#064134')
s2.grid(column=3)

s3 = Label(root, text="             ", bg='#064134')
s3.grid(column=4)
photo3 = PhotoImage(file="../View/Pictures/share.png")


def callback3():
    root.destroy()
    os.system('SharedAct.py')


sharedBtn = Button(root, image=photo3, width=225, height=225, padx=100, command=callback3)
sharedBtn.grid(row=3, column=5)
shLb = Label(root, text='Shared Activity', font=5, pady=10, bg='#064134', fg='white')
shLb.grid(row=2, column=5)

l = Label(root, text='    ', bg="#064134")
l.grid(row=4, column=3)

l2 = Label(root, text='    ', bg="#064134")
l2.grid(row=5, column=3)

l3 = Label(root, text='    ', bg="#064134")
l3.grid(row=6, column=3)
photo4 = PhotoImage(file="../View/Pictures/back.png")


def callback4():
    root.destroy()
    os.system('options.py')


backBtn = Button(root, image=photo4, command=callback4, borderwidth=0)
backBtn.grid(row=7, column=3)
root.mainloop()
