from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import ttk
import os
import sys
root = Tk()

root.title("Searching For An Activity")
root['background']='#064134'
root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
title=Label(root,text='         Create your own activity',bg='#064134',pady=20,font=20,fg='orange')
title.grid(row=0,column=2)

vlist=["Easy","Medium","Hard"]
Combo = ttk.Combobox(root, values=vlist)
Combo.set("select level")
Combo.grid(row=1,column=1,ipadx=10)

vlist=["math","science"]
filedCombo = ttk.Combobox(root, values=vlist)
filedCombo.set("select filed")
filedCombo.grid(row=1,column=2,ipadx=10)

vlist=["English","Hebrew","Arabic"]
lanCombo = ttk.Combobox(root, values=vlist)
lanCombo.set("select language")
lanCombo.grid(row=1,column=3,ipadx=10)

slb=Label(root,bg='#064134' ,text='     ')
slb.grid(row=2,column=2)
ques=Label(root,text='Add Question to your activity ',bg='#064134',font=10,fg='white')
ques.grid(row=3, column=2)
slb2=Label(root,bg='#064134' ,text='     ')
slb2.grid(row=4,column=2)
quesEntry=Entry(root)
quesEntry.grid(row=5,column=2,ipadx=100)

Addphoto = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/Add.png")
Addbtn=Button(root,image=Addphoto,padx=100,bd=0,bg='#064134')
Addbtn.grid(row=5,column=3)

anslb=Label(root,text="Add Three Possible Answers",bg='#064134',font=10,fg='white')
anslb.grid(row=6 ,column=2)
AnsEntry=Entry(root)
AnsEntry.grid(row=7,column=2,ipadx=100)

Addphoto2 = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/Add.png")
Addbtn=Button(root,image=Addphoto2,padx=100,bd=0,bg='#064134')
Addbtn.grid(row=7,column=3)


def callback4():
    os.system('MainMenu.py')
photo4 = PhotoImage(file="C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/back.png")
backbtn=Button(root,image=photo4,command=callback4,borderwidth=0,bg='#064134')
backbtn.grid(row=8,column=2)

root.mainloop()