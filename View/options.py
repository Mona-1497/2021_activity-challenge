from tkinter import *
import os


root = Tk()

root.title("Create")
root['background'] = '#064134'
root.geometry("1000x1000")

def call1():
    root.destroy()
    os.system('SearchAndChooseAct.py')
Button(root,text="Questions",command=call1,bg='#064134',fg='yellow',font=10,bd=0).place(x=300,y=50)

def call2():
    root.destroy()
    os.system('chooseRiddle.py')
Button(root,text="Riddles",command=call2,bg='#064134',fg='yellow',font=10,bd=0).place(x=300,y=100)

def call3():
    root.destroy()
    os.system('play.py')
Button(root,text="Classifications",command=call3,bg='#064134',fg='yellow',bd=0,font=10).place(x=300,y=150)

def call4():
    root.destroy()
    os.system('chooseMatch.py')
Button(root,text="Matches",command=call4,bg='#064134',fg='yellow',bd=0,font=10).place(x=300,y=200)
def back():
    root.destroy()
    os.system('MainMenu.py')
photo = PhotoImage(file="../View/Pictures/back.png")
mybtn=Button(root,image=photo,bg='#F39C12',pady=10,padx=20,command=back)
mybtn.place(x=300,y=400)
root.mainloop()

