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

class Match():
    def __init__(self, field, description):
        self.field = field
        self.description = description
        self.currentID = 0
        self.matches = []


    def define_match(self):
        mycursor.execute("""INSERT INTO matches(field,description)
                                VALUES (%s, %s)""", (self.field, self.description))
        x = mycursor.getlastrowid()
        self.currentID = x
        mydb.commit()


    def addmatch(self,value,matchTo):
        self.matches.append({value: matchTo})
        x = []
        for key, values in self.matches[len(self.matches) - 1].items():
            x.append(key)
            x.append(values[0])
            mycursor.execute("""
                              INSERT INTO matching(MatchingID,value,ismachTo)
                              VALUES (%s,%s, %s)""", (self.currentID, x[0], x[1]))
        mydb.commit()
def add_match_page(root):
    match=Match(filedCombo.get(),description.get("1.0",END))
    match.define_match()
    root.destroy()
    root1=Tk()
    root1['background'] = '#064134'
    root1.geometry("1000x1000")
    title = Label(root1, text="Matching Card Values", fg='yellow', font=100, bg='#064134')
    title.place(x=400, y=40)
    firstcard=Label(root1,text='vlaue',fg='white',font=10,bg='#064134')
    firstcard.place(x=200,y=100)
    e1=Entry(root1)
    e1.place(x=200,y=140)
    secondcard = Label(root1, text='matching to', fg='white', font=10, bg='#064134')
    secondcard.place(x=400, y=100)
    e2= Entry(root1)
    e2.place(x=400, y=140)

    Addphoto2 = PhotoImage(file="../View/Pictures/Add.png")
    for i in range(10):
        Addbtn = Button(root1, image=Addphoto2, padx=100, bd=0, bg='#064134',command=lambda: match.addmatch(e1.get(),e2.get()))

    Addbtn.place(x=300,y=200)

    def back():
        root1.destroy()
        os.system('MainMenu.py')

    photo = PhotoImage(file="../View/Pictures/back.png")
    mybtn = Button(root1, image=photo, bg='#F39C12', pady=10, padx=20, command=back)
    mybtn.place(x=300, y=300)
    root1.mainloop()

root=Tk()
root['background']='#064134'
root.geometry("1000x1000")
title=Label(root,text="Create Match",fg='green',font=50,bg='#064134')
title.place(x=400,y=40)
vlist=["biology","chemistry","physics",'math']
filedCombo = ttk.Combobox(root, values=vlist)
filedCombo.set("choose filed")
filedCombo.place(x=300,y=100)
Label(root,text="Match Description: ",bg='#064134',font=10,fg="white").place(x=300,y=140)
description=Text(root,width=20,height=10)
description.place(x=300,y=180)
Addimg = PhotoImage(file = "../View/Pictures/Add.png")

addbtn=Button(root,image=Addimg,bd=0,bg='#064134',command=lambda :add_match_page(root))
addbtn.place(x=300,y=350)
def back():
    root.destroy()
    os.system('createoptions.py')
photo = PhotoImage(file="../View/Pictures/back.png")
mybtn=Button(root,image=photo,bg='#F39C12',pady=10,padx=20,command=back)
mybtn.place(x=300,y=450)




root.mainloop()