from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import os
import mysql.connector
import openpyexcel
from tkinter import messagebox
from openpyexcel.utils.exceptions import InvalidFileException

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mona100%",
    database="ActivityChallengeDB",
)

def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


mycursor = mydb.cursor(buffered=True)
i=0

class Activity:
    def __init__(self,level,filed,questionNum,description):
        self.level=level
        self.filed=filed
        self.questionNum=questionNum
        self.currentID = 0
        self.questions=[]
        self.decription=description


        #currentID=mycursor.lastrowid


    def addactivity(self):

         mycursor.execute("""INSERT INTO AddActivity (level,filed,questionNum,description)
                           VALUES (%s, %s, %s,%s)""", (self.level, self.filed, self.questionNum,self.decription))
         global x
         x = mycursor.lastrowid
         self.currentID = x
         mydb.commit()
        #os.system('createAct.py')
    def addQuestion(self,question, answer1, answer2, answer3,correctans,Addbtn,resbtn,root,importbtn):
        global i
        i = i + 1
        if i <=int(self.questionNum):
          if(question=="") or(answer1=="") or(answer2=="") or(answer3=="") or (correctans==""):
             mylabel.config(text="invalid values!!")
             i=i-1
             return
          for k in range(len(self.questions)):
              for key, values in self.questions[k].items():

               if key == question:
                  mylabel.config(text="duplicate value, please insert card again")
                  i = i - 1
                  return

          else:

           self.questions.append({question: (answer1, answer2, answer3, correctans)})
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
           mylabel.config(text="added question "+str(i))
           if i==int(self.questionNum):
            Addbtn.place_forget()
            resbtn.place_forget()
            importbtn.place_forget()
            #mylabel.config(text='')
            Label(root, text='your Activity is completed!', bg='#064134', fg='orange',
                  font=("Comic Sans MS", 15)).place(x=700, y=350)






def addQuestionPage(root1):
    global mylabel
    if (Combo.get() == 'select level') or (filedCombo.get() == 'select field'):
        Label(root1, text='please choose valid values', bg='#064134', fg='orange', font=("Comic Sans MS", 15)).place(x=500, y=520)
        return

    activity = Activity(Combo.get(), filedCombo.get(), w.get(),description.get("1.0",END))
    activity.addactivity()
    num=w.get()
    root1.destroy()
    #os.system('createAct.py')
    root = Tk()
    root.title("Add Questions")
    root['background'] = '#064134'
    root.geometry("1920x1080")

    ques = Label(root, text='Add Question To Your Activity ', bg='#064134', fg='orange',font=("Comic Sans MS", 15))
    ques.place(x=700,y=50)

    quesEntry = Entry(root,width=50)
    quesEntry.place(x=700,y=100)

    anslb = Label(root, text="Add Three Possible Answers", bg='#064134', fg='orange',font=("Comic Sans MS", 15))
    anslb.place(x=700,y=150)
    Ans1Entry = Entry(root,width=50)
    Ans1Entry.place(x=700,y=200)
    Ans2Entry = Entry(root,width=50)
    Ans2Entry.place(x=700,y=220)
    Ans3Entry = Entry(root,width=50)
    Ans3Entry.place(x=700,y=240)
    clb = Label(root, text="Add The Correct Answer", bg='#064134',fg='orange',font=("Comic Sans MS", 15))
    clb.place(x=700,y=280)
    correctAns = Entry(root,width=50)
    correctAns.place(x=700,y=320)
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/reset.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(resized_image)
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addimg.png"))
    resized_image = img.resize((60, 60), Image.ANTIALIAS)
    Addphoto2 = ImageTk.PhotoImage(resized_image)

    Label(root,text='Add Questions By Importing Excel File', bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=220,y=50)
    pathEntry=Entry(root,width=50)
    pathEntry.insert(0,'file path ')
    pathEntry.place(x=220,y=100)
    sheetEntry=Entry(root,width=50)
    sheetEntry.insert(0,'sheet name')
    sheetEntry.place(x=220,y=150)

    def delete():
        mylabel.config(text="")
        quesEntry.delete(0,'end')
        Ans1Entry.delete(0,'end')
        Ans2Entry.delete(0,'end')
        Ans3Entry.delete(0,'end')
        correctAns.delete(0,'end')

    def importfile(lb):
     lb.config(text='')
     if not os.path.isfile(pathEntry.get()):
         lb.config(text='please check file format')
         return


     wb = openpyexcel.load_workbook(pathEntry.get())
     if sheetEntry.get() in wb.sheetnames:
        sh = wb[sheetEntry.get()]
        row = sh.max_row
        for i in range(2, row + 1):
            activity.addQuestion(sh[i][0].value,sh[i][1].value,sh[i][2].value,sh[i][3].value,sh[i][4].value,Addbtn,resetbtn,root,importbtn)
        lb.config(text='file imported successfully')
     else:
      lb.config(text="sheet doesn't exists")

    lb = Label(root, text='', bg='#064134', fg='orange',font=("Comic Sans MS", 15))
    lb.place(x=320, y=200)
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/import.png"))
    resized_image = img.resize((80, 70), Image.ANTIALIAS)
    importphoto = ImageTk.PhotoImage(resized_image)
    importbtn = Button(root,image=importphoto,text='import',bg='#064134',bd=0, command=lambda :importfile(lb))
    importbtn.place(x=220, y=200)


    Addbtn = Button(root, image=Addphoto2, padx=100, bd=0, bg='#064134',
                     command=lambda: activity.addQuestion(quesEntry.get(), Ans1Entry.get(), Ans2Entry.get(),
                                              Ans3Entry.get(),correctAns.get(),Addbtn,resetbtn,root,importbtn))
    resetbtn=Button(root,image=photo2,command=delete,padx=20,bd=0,bg='#064134')



    Addbtn.place(x=750, y=360)
    resetbtn.place(x=850, y=355)
    mylabel = Label(root, text='', bg='#064134',fg='orange',font=("Comic Sans MS", 15))
    mylabel.place(x=700, y=450)

    def callback4():
          root.destroy()
          os.system('Activity.py')



    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(resized_image)
    backbtn = Button(root, image=photo4, command=callback4, borderwidth=0,bg='#064134',bd=0)
    backbtn.place(x=20,y=580)

    def home():

          if i<int(num):
              response=messagebox.askyesno("?!",'activity not completed,do you want to leave?!')
              ##don't wan't to continue activity
              if response==1:
                  #x = mycursor.lastrowid
                  currentID = x
                  print(x)
                  sql='DELETE FROM addactivity WHERE id=%s'
                  mycursor.execute(sql,(currentID,))
                  mydb.commit()
                  root.destroy()
                  os.system('MainMenu.py')


          else:
            root.destroy()
            os.system('MainMenu.py')


    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    photo5 = ImageTk.PhotoImage(resized_image)
    homebtn = Button(root, image=photo5, command=home, borderwidth=0, bg='#064134')
    homebtn.place(x=20, y=8)
    root.mainloop()

root=Tk()
root.title("create activity")
root['background']='#064134'
root.geometry("1920x1080")
title=Label(root,text='Create your activity',bg='#064134', fg='orange',font=("Comic Sans MS", 20))
title.place(x=500,y=40)


vlist=["Easy","Medium","Hard"]
Combo = ttk.Combobox(root, values=vlist)
Combo.set("select level")
Combo.place(x=570,y=125)
Label(root,text='level',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=120)

vlist=["biology","chemistry","physics","math"]
filedCombo = ttk.Combobox(root, values=vlist)
filedCombo.set("select field")
filedCombo.place(x=570,y=185)
Label(root,text='field',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=180)

w = Spinbox(root, from_=1, to=15)
w.place(x=570,y=245)
Label(root,text='questions number',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=240)
Label(root,text='description',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=300)
description=Text(root,width=20,height=5)
description.place(x=560,y=300)

#Addimg = PhotoImage(file = "..//Pictures/Add.png")
#aa = Activity(Combo.get(),filedCombo.get(),lanCombo.get())
Addimg = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addimg.png"))
resized_image = Addimg.resize((90, 80), Image.ANTIALIAS)
Addimg = ImageTk.PhotoImage(resized_image)
Addquesbtn=Button(root,image=Addimg,padx=100,bd=0,bg='#064134',command=lambda:addQuestionPage(root))
Addquesbtn.place(x=550,y=430)
def back():
    root.destroy()
    os.system('createoptions.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,pady=10,padx=20,command=back,bg='#064134',bd=0)
mybtn.place(x=20,y=580)


def callback4():
    root.destroy()
    os.system('MainMenu.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(resized_image)
homebtn = Button(root, image=photo4, command=callback4, borderwidth=0, bg='#064134')
homebtn.place(x=20, y=20)
root.mainloop()


