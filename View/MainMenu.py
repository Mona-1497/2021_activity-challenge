from tkinter import *
import os


root = Tk()

root.title("Main Menu")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
title = Label(root, text='       Main Menu', bg='#064134', font=30, fg='white', pady=10)
title.grid(row=0, column=2)


def callback():
    os.system('SearchAndChooseAct.py')


photo = PhotoImage(file="../View/Pictures/play.png")
startBtn = Button(root, image=photo, padx=100, bd=0, command=callback)
startBtn.grid(row=1, column=1)

createPhoto = PhotoImage(file="../View/Pictures/create.png")
createBtn = Button(root, image=createPhoto, padx=100, bd=0)
createBtn.grid(row=1, column=2)

instPhoto = PhotoImage(file="../View/Pictures/instructions.png")
instBtn = Button(root, image=instPhoto, padx=100, bd=0)
instBtn.grid(row=1, column=3)

proPhoto = PhotoImage(file="../View/Pictures/profile.png")
profileBtn = Button(root, image=proPhoto, padx=100, bd=0)
profileBtn.grid(row=2, column=1)

groupPhoto = PhotoImage(file="../View/Pictures/groups.png")
groupBtn = Button(root, image=groupPhoto, padx=100, bd=0)
groupBtn.grid(row=2, column=2)

root.mainloop()