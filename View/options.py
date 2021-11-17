from tkinter import *
import os

from PIL import ImageTk,Image

root = Tk()

root.title("Start Activity")
root['background'] = '#064134'
root.geometry("1920x1080")
Label(root,text="Play!",font=("Comic Sans MS", 30,"bold"),bg= '#064134',fg='orange').place(x=550,y=15)

def call1():
     root.destroy()
     os.system('SearchAndChooseAct.py')



img= (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/ques3.png"))
resized_image= img.resize((200,200), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
Label(root,text=' Questions',font=("Comic Sans MS",15),bg= '#064134',fg='orange').place(x=150 ,y=150)
Button(root,image=new_image,command=call1,bg='#064134',fg='yellow',font=10,bd=0).place(x=100,y=190)

def call2():
    root.destroy()
    os.system('chooseRiddle.py')

img= (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/rid2.png"))
resized_image= img.resize((200,200), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image)
Label(root,text=' Riddles',font=("Comic Sans MS",15),bg= '#064134',fg='orange').place(x=450 ,y=150)
Button(root,image=new_image2,command=call2,bg='#064134',fg='yellow',font=10,bd=0).place(x=400,y=190)

def call3():
    root.destroy()
    os.system('play.py')
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/class2.png"))
resized_image = img.resize((200, 200), Image.ANTIALIAS)
new_image3 = ImageTk.PhotoImage(resized_image)
Label(root,text=' Classifications',font=("Comic Sans MS",15),bg= '#064134',fg='orange').place(x=725 ,y=150)
Button(root,image=new_image3,command=call3,bg='#064134',fg='yellow',bd=0,font=10).place(x=700,y=190)
def call4():
    root.destroy()
    os.system('chooseMatch.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/mem2.png"))
resized_image = img.resize((200, 200), Image.ANTIALIAS)
new_image4 = ImageTk.PhotoImage(resized_image)
Label(root,text=' Matches',font=("Comic Sans MS",15),bg= '#064134',fg='orange').place(x=1050 ,y=150)
Button(root,image=new_image4,command=call4,bg='#064134',fg='yellow',bd=0,font=10).place(x=1000,y=190)
def back():
    root.destroy()
    os.system('MainMenu.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
new_image5 = ImageTk.PhotoImage(resized_image)
#photo = PhotoImage(file="../View/Pictures/back.png")
mybtn=Button(root,image=new_image5,command=back,bd=0,bg='#064134')
mybtn.place(x=20,y=580)
root.mainloop()

