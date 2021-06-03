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

def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


mycursor = mydb.cursor(buffered=True)
class Activity:
    def __init__(self,level,filed,language):
        self.level=level
        self.filed=filed
        self.language=language
        self.currentID = 0
        self.questions = []

        #currentID=mycursor.lastrowid


    def addactivity(self):

        mycursor.execute("""INSERT INTO AddActivity (level,filed,language)
                    VALUES (%s, %s, %s)""",(self.level,self.filed,self.language))
        x = mycursor.getlastrowid()
        self.currentID = x
        mydb.commit()
        #os.system('createAct.py')

    def addQuestion(self,question, answer1, answer2, answer3,correctans):
        self.questions.append({question: (answer1, answer2, answer3,correctans)})

        x = []
        for key, values in self.questions[len(self.questions) - 1].items():
            x.append(key)
            x.append(values[0])
            x.append(values[1])
            x.append(values[2])
            x.append(values[3])

        mycursor.execute("""
                            INSERT INTO questions (ActivityID,question,answer1,answer2,answer3,CorrectAnswer)
                            VALUES (%s,%s, %s, %s, %s,%s)""", (self.currentID, x[0], x[1], x[2], x[3],x[4]))
        mydb.commit()



def addQuestionPage(root1):
    activity = Activity(Combo.get(), filedCombo.get(), lanCombo.get())
    activity.addactivity()
    root1.destroy()
    #os.system('createAct.py')
    root = Tk()

    root.title("Add Questions")
    root['background'] = '#064134'
    root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
    root.geometry("1000x1000")
    title = Label(root, text='         Create your own activity', bg='#064134', pady=20, font=20, fg='orange')
    title.grid(row=0, column=2)

    slb = Label(root, bg='#064134', text='     ')
    slb.grid(row=2, column=2)
    ques = Label(root, text='Add Question to your activity ', bg='#064134', font=10, fg='white')
    ques.grid(row=3, column=2)
    slb2 = Label(root, bg='#064134', text='     ')
    slb2.grid(row=4, column=2)
    quesEntry = Entry(root)
    quesEntry.grid(row=5, column=2, ipadx=100)

    anslb = Label(root, text="Add Three Possible Answers", bg='#064134', font=10, fg='white')
    anslb.grid(row=6, column=2)
    Ans1Entry = Entry(root)
    Ans1Entry.grid(row=7, column=2, ipadx=100)
    Ans2Entry = Entry(root)
    Ans2Entry.grid(row=8, column=2, ipadx=100)
    Ans3Entry = Entry(root)
    Ans3Entry.grid(row=9, column=2, ipadx=100)
    clb = Label(root, text="Add The Correct Answer", bg='#064134', font=10, fg='white')
    clb.grid(row=10, column=2)
    correctAns = Entry(root)
    correctAns.grid(row=11, column=2, ipadx=100)
    Addphoto2 = PhotoImage(file="C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/Add.png")
    resetimg = PhotoImage(file="../View/Pictures/reset.png")

    def delete():
        quesEntry.delete(0,'end')
        Ans1Entry.delete(0,'end')
        Ans2Entry.delete(0,'end')
        Ans3Entry.delete(0,'end')
        correctAns.delete(0,'end')
    for i in range(10):
        Addbtn = Button(root, image=Addphoto2, padx=100, bd=0, bg='#064134',
                    command=lambda: activity.addQuestion(quesEntry.get(), Ans1Entry.get(), Ans2Entry.get(),
                                              Ans3Entry.get(),correctAns.get()))
        resetbtn=Button(root,image=resetimg,command=delete,padx=20,bd=0,bg='#064134')


    Addbtn.grid(row=15, column=2,padx=20)
    resetbtn.grid(row=12 ,column=2)

    def callback4():
        root.destroy()
        os.system('MainMenu.py')

    photo4 = PhotoImage(file="C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/back.png")
    backbtn = Button(root, image=photo4, command=callback4, borderwidth=0, bg='#064134')
    backbtn.grid(row=20, column=2)

    root.mainloop()

root=Tk()
root.title("create activity")
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
filedCombo.set("select field")
filedCombo.grid(row=1,column=2,ipadx=10)

vlist=["English","Hebrew","Arabic"]
lanCombo = ttk.Combobox(root, values=vlist)
lanCombo.set("select language")
lanCombo.grid(row=1,column=3,ipadx=10)

Addimg = PhotoImage(file = "C:/Users/Mona_/PycharmProjects/2021_activity-challenge/Model/Add.png")
#aa = Activity(Combo.get(),filedCombo.get(),lanCombo.get())

Addquesbtn=Button(root,image=Addimg,padx=100,bd=0,bg='#064134',command=lambda:addQuestionPage(root))
Addquesbtn.grid(row=2,column=2)
def back():
    root.destroy()
    os.system('createoptions.py')
photo = PhotoImage(file="../View/Pictures/back.png")
mybtn=Button(root,image=photo,bg='#F39C12',pady=10,padx=20,command=back)
mybtn.place(x=200,y=200)
root.mainloop()


