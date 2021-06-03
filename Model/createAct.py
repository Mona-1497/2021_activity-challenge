from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import ttk
import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mona100%",
    database="ActivityChallengeDB"
)

mycursor = mydb.cursor(buffered=True)

class createAct:
    def __init__(self, level, filed, language, question, answer1, answer2, answer3):
        self.level=level
        self.filed=filed
        self.language=language
        self.question=question
        self.ans1=answer1
        self.ans2=answer2
        self.ans3=answer3

    def activity(self):
            mycursor.execute("""INSERT INTO activities(level,filed, language, question, answer1, answer2,answer3) VALUES (
                     %s, %s, %s, %s, %s,%s,%s)""",
                             (self.level, self.filed, self.language, self.question, self.ans1, self.ans2, self.ans3))
            mydb.commit()

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


anslb=Label(root,text="Add Three Possible Answers",bg='#064134',font=10,fg='white')
anslb.grid(row=6 ,column=2)
Ans1Entry=Entry(root)
Ans1Entry.grid(row=7,column=2,ipadx=100)
Ans2Entry=Entry(root)
Ans2Entry.grid(row=8,column=2,ipadx=100)
Ans3Entry=Entry(root)
Ans3Entry.grid(row=9,column=2,ipadx=100)

Addphoto2 = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/Add.png")
Addbtn=Button(root,image=Addphoto2,padx=100,bd=0,bg='#064134',command=lambda: createAct(Combo.get(),
        filedCombo.get(),lanCombo.get(),quesEntry.get(), Ans1Entry.get(),Ans2Entry.get(),Ans3Entry.get()).activity())
Addbtn.grid(row=10,column=2)


def callback4():
    os.system('MainMenu.py')
photo4 = PhotoImage(file="C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/back.png")
backbtn=Button(root,image=photo4,command=callback4,borderwidth=0,bg='#064134')
backbtn.grid(row=11,column=2)

root.mainloop()