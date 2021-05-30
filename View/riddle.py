from tkinter import *
from tkinter import ttk
import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mona100%",
    database="ActivityChallengeDB"
)

def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


mycursor = mydb.cursor(buffered=True)

class Riddle():
    def __init__(self,filed,subject):
        self.filed=filed
        self.subject=subject
        self.currentID=0
        self.riddles=[]

    def define_riddle(self):
        mycursor.execute("""INSERT INTO AddRiddle (filed,subject)
                            VALUES (%s, %s)""", (self.filed, self.subject))
        x = mycursor.getlastrowid()
        self.currentID = x
        mydb.commit()

    def addRiddle(self, riddle,answer,explanation):
        self.riddles.append({riddle: (answer,explanation)})

        x = []
        for key, values in self.riddles[len(self.riddles) - 1].items():
            x.append(key)
            x.append(values[0])
            x.append(values[1])

        mycursor.execute("""
                               INSERT INTO riddle(RiddleID,riddle,answer,explanation)
                               VALUES (%s,%s, %s,%s)""", (self.currentID, x[0], x[1],x[2]))
        mydb.commit()


def add_riddle_page(root1):
    riddle=Riddle(filedCombo.get(),sub.get())
    riddle.define_riddle()
    root1.destroy()
    root=Tk()
    root['background'] = '#064134'
    root.geometry("1000x1000")
    title = Label(root, text="Write Riddle", fg='yellow', font=100, bg='#064134')
    title.place(x=400, y=40)
    text=Text(root, height=10, width=30)
    text.place(x=350, y=100)


    ans_entry=Entry(root)
    ans_entry.place(x=400,y=300)
    text_exp=Text(root, height=10, width=30)
    text_exp.place(x=350, y=350)
    Addphoto2 = PhotoImage(file="../View/Pictures/Add.png")
    resetimg = PhotoImage(file="../View/Pictures/reset.png")

    def delete():
        text.delete("1.0", END)
        ans_entry.delete(0, 'end')
        text_exp.delete("1.0", END)


    for i in range(10):
        Addbtn = Button(root, image=Addphoto2, padx=100, bd=0, bg='#064134',
                        command=lambda: riddle.addRiddle(text.get("1.0",END), ans_entry.get(),text_exp.get("1.0",END)))
        resetbtn = Button(root, image=resetimg, command=delete, padx=20, bd=0, bg='#064134')

    resetbtn.place(x=650,y=200)
    Addbtn.place(x=650,y=280)
    root.mainloop()

root=Tk()
root['background']='#064134'
root.geometry("1000x1000")
title=Label(root,text="Create Riddle",fg='green',font=50,bg='#064134')
title.place(x=400,y=40)
vlist=["biology","chemistry","physics",'math']
filedCombo = ttk.Combobox(root, values=vlist)
filedCombo.set("choose filed")
filedCombo.place(x=300,y=100)

sub=Entry(root)
sub.insert(0,"enter subject")
sub.place(x=300,y=140)

Addimg = PhotoImage(file = "../View/Pictures/Add.png")

addbtn=Button(root,image=Addimg,bd=0,bg='#064134',command=lambda :add_riddle_page(root))
addbtn.place(x=400,y=180)
root.mainloop()


