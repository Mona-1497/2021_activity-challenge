import os
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk,Image

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
i=0
class Classification:
    def __init__(self, filed,description,first_column, second_column,cardsNum):
        self.filed=filed
        self.description=description
        self.first_column = first_column
        self.second_column = second_column
        self.cardsNum=cardsNum
        self.answers = []


    def add_classification(self):
        mycursor.execute("""INSERT INTO classification(filed,description,firstgroup,secondgroup,CardsNum)
                    VALUES (%s, %s, %s,%s,%s)""",(self.filed,self.description,self.first_column,self.second_column,self.cardsNum))
        global x1
        x1 = mycursor.lastrowid
        self.currentID = x1
        mydb.commit()

    def add_answer(self,classified_to,answer,Addbtn,root,Resbtn):
        if classified_to=="card's group" or answer=="card value":
            mylabel.config(text='please,insert valid values ')
            return
        global i
        i = i + 1
        if i<=int(self.cardsNum):
          for k in range (len(self.answers)):
                if self.answers[k][1]==answer:
                    mylabel.config(text="duplicate value, please insert card again")
                    i=i-1
                    return

          self.answers.append((classified_to,answer))

          mycursor.execute("""
                                   INSERT INTO answers(classificationid,classifiedTo,answer)
                                   VALUES (%s,%s, %s)""", (self.currentID,classified_to,answer))
          mydb.commit()
          mylabel.config(text='added card  '+str(i))
          if i==int(self.cardsNum):
            Addbtn.place_forget()
            Resbtn.place_forget()
            #mylabel.config(text='')
            Label(root, text='your Activity is completed!', bg='#064134', fg='orange',
                  font=("Comic Sans MS", 15)).place(x=500, y=240)




def creat(root1):
    global mylabel
    if(filedEntry.get()=='select field') or(descEntry.get()=='')or(e1.get()=='')or(e2.get()==''):
        Label(root1, text='please choose valid values', bg='#064134', fg='orange', font=("Comic Sans MS", 15)).place(x=450, y=550)
        return
    classification=Classification(filedEntry.get(),descEntry.get(),e1.get(),e2.get(),w.get())
    classification.add_classification()
    x = e1.get()
    y = e2.get()
    num=w.get()
    root1.destroy()
    root2=Tk()
    root2.geometry("1920x1080")
    root2['background'] = '#064134'
    root2.title("classification cards")
    Label(root2,text="classification cards",bg='#064134', fg='orange',font=("Comic Sans MS", 20)).place(x=500,y=40)
    answer = Entry(root2,width=40)
    answer.insert(0,"card value")
    answer.place(x=500, y=210)
    vlist=[x,y]
    classifiedTo = ttk.Combobox(root2, values=vlist,width=40)
    classifiedTo.set("card's group")
    classifiedTo.place(x=500, y=150)
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addimg.png"))
    resized_image = img.resize((60, 60), Image.ANTIALIAS)
    Addimg = ImageTk.PhotoImage(resized_image)
    Addbtn=Button(root2, image=Addimg,bd=0,bg='#064134', command= lambda: classification.add_answer(classifiedTo.get(),answer.get(),Addbtn,root2,Resbtn))
    Addbtn.place(x=500, y=300)
    mylabel=Label(root2,text='',bg='#064134',font=("Comic Sans MS", 15),fg='orange')
    mylabel.place(x=530,y=400)
    def back():
        root2.destroy()
        os.system('createoptions.py')

    def delete():
        answer.delete(0,'end')
        classifiedTo.set("select answer group")
        mylabel.config(text="")

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    bbphoto = ImageTk.PhotoImage(resized_image)
    #mybtn = Button(root2, image=bbphoto, pady=10, padx=20, command=back,bd=0,bg='#064134')
   # mybtn.place(x=20, y=580)


    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/reset.png"))
    resized_image = img.resize((80, 50), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    Resbtn=Button(root2, image=photo, command=delete,bd=0,bg='#064134')
    Resbtn.place(x=650,y=300)

    def home():
        if i < int(num):
            response = messagebox.askyesno("?!", 'activity not completed,do you want to leave?!')
            ##don't wan't to continue activity
            if response == 1:
                # x = mycursor.lastrowid
                currentID = x1
                sql = 'DELETE FROM classification WHERE id=%s'
                mycursor.execute(sql, (currentID,))
                mydb.commit()
        root2.destroy()
        os.system('MainMenu.py')


    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(resized_image)
    homebtn = Button(root2, image=photo4, command=home, borderwidth=0, bg='#064134')
    homebtn.place(x=20, y=20)
    root2.mainloop()




root=Tk()
root.geometry("1920x1080")
root['background']='#064134'
root.title("create classification")
title=Label(root,text="Create Classification",bg='#064134',font=("Comic Sans MS", 20),fg='orange')
title.place(x=500,y=40)
l1=Label(root,text=" first column name",bg='#064134',font=("Comic Sans MS", 15),fg='orange')
l1.place(x=400,y=120)
e1=Entry(root)
e1.place(x=650,y=125)
l2=Label(root,text=" second column name",bg='#064134',font=("Comic Sans MS", 15),fg='orange')
l2.place(x=400,y=180)
e2=Entry(root)
e2.place(x=650,y=185)
Label(root,text='field',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=240)
vlist=["biology","chemistry","physics",'math']
filedEntry = ttk.Combobox(root, values=vlist)
filedEntry.set("select field")
filedEntry.place(x=650,y=245)
Label(root,text='description',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=300)

descEntry=Entry(root)
descEntry.place(x=650,y=305)
Label(root,text='cards number',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=360)
w = Spinbox(root, from_=1, to=15)
w.place(x=650,y=365)

#Addimg = PhotoImage(file = "..//Pictures/Add.png")
Addimg = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addimg.png"))
resized_image = Addimg.resize((90, 80), Image.ANTIALIAS)
Addimg = ImageTk.PhotoImage(resized_image)
btn=Button(root,image=Addimg,bg='#064134',bd=0,command=lambda:creat(root))
btn.place(x=500,y=450)
def back():
    root.destroy()
    os.system('createoptions.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,pady=10,padx=20,command=back,bd=0,bg='#064134')
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