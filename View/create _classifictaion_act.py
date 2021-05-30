from tkinter import *
from tkinter import ttk
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

class Classification:
    def __init__(self, filed,description,first_column, second_column):
        self.filed=filed
        self.description=description
        self.first_column = first_column
        self.second_column = second_column
        self.answers = []


    def add_classification(self):
        mycursor.execute("""INSERT INTO classification(filed,description,firstgroup,secondgroup)
                    VALUES (%s, %s, %s,%s)""",(self.filed,self.description,self.first_column,self.second_column))
        x = mycursor.getlastrowid()
        self.currentID = x
        mydb.commit()

    def add_answer(self,classified_to,answer):
        self.answers.append((classified_to,answer))
        print(classified_to)

        mycursor.execute("""
                                   INSERT INTO answers(classificationid,classifiedTo,answer)
                                   VALUES (%s,%s, %s)""", (self.currentID,classified_to,answer))
        mydb.commit()


def creat(root1):
    classification=Classification(filedEntry.get(),descEntry.get(),e1.get(),e2.get())
    classification.add_classification()
    x = e1.get()
    y = e2.get()
    root1.destroy()
    root2=Tk()
    root2.geometry("1000x1000")
    root2['background'] = '#064134'
    Label(root2,text="insert answer",bg='#064134',fg="white").place(x=319,y=180)
    answer = Entry(root2)
    answer.place(x=300, y=210)
    vlist=[x,y]
    classifiedTo = ttk.Combobox(root2, values=vlist)
    classifiedTo.set("select answer group")
    classifiedTo.place(x=300, y=150)
    Button(root2, text="Add Answer", bg='orange', command= lambda: classification.add_answer(classifiedTo.get(),answer.get())).place(x=330, y=240)
    root2.mainloop()




root=Tk()
root.geometry("1000x1000")
root['background']='#064134'
title=Label(root,text="Classification Activity",bg='#064134',font=20,fg='red')
title.place(x=400,y=40)
l1=Label(root,text="insert first column name",bg='#064134',font=20,fg='white')
l1.place(x=80,y=100)
e1=Entry(root)
e1.place(x=130,y=140)
l2=Label(root,text="insert second column name",bg='#064134',font=20,fg='white')
l2.place(x=400,y=100)
e2=Entry(root)
e2.place(x=450,y=140)
Label(root,text='field',bg='#064134',fg='white',font=20).place(x=250,y=195)
filedEntry=Entry(root)
filedEntry.place(x=300,y=200)
Label(root,text='description',bg='#064134',fg='white',font=20).place(x=200,y=235)

descEntry=Entry(root)
descEntry.place(x=300,y=240)

Addimg = PhotoImage(file = "../View/Pictures/Add.png")
btn=Button(root,image=Addimg,bg='#064134',command=lambda :creat(root))
btn.place(x=280,y=280)

root.mainloop()