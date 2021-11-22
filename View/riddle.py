from tkinter import *
from tkinter import ttk
import os
import mysql.connector
from PIL import ImageTk,Image
import openpyexcel
from future.moves.tkinter import messagebox
from openpyexcel.utils.exceptions import InvalidFileException

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
class Riddle():
    def __init__(self,filed,subject,riddlesNum):
        self.filed=filed
        self.subject=subject
        self.currentID=0
        self.riddlesNum=riddlesNum
        self.riddles=[]

    def define_riddle(self):
        mycursor.execute("""INSERT INTO AddRiddle (filed,subject,riddlesNum)
                            VALUES (%s, %s,%s)""", (self.filed, self.subject,self.riddlesNum))
        global x
        x = mycursor.lastrowid
        self.currentID = x
        mydb.commit()

    def addRiddle(self, riddle,answer,explanation,addbtn,resetbtn,importbtn,root):
        global i
        i = i + 1
        if i <= int(self.riddlesNum):
          if (riddle=="Riddle") or (riddle=="") or (answer=="Riddle Answer") or (answer=="") or (explanation=="Riddle Explaination") or (explanation==""):
               mylabel.config(text="invalid values!!")
               i = i - 1
               return
          for k in range(len(self.riddles)):
              for key, values in self.riddles[k].items():

               if key == riddle:
                  mylabel.config(text="duplicate value, please insert card again")
                  i = i - 1
                  return
          else:
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
            mylabel.config(text='Riddle ' + str(i)+' Added!')
            if i == int(self.riddlesNum):
             addbtn.place_forget()
             resetbtn.place_forget()
             importbtn.place_forget()
             #mylabel.config(text='')
             Label(root, text='your Activity is completed!', bg='#064134', fg='orange',
                  font=("Comic Sans MS", 15)).place(x=550, y=550)




def add_riddle_page(root1):
    global mylabel
    if(filedCombo.get()=='select field') or(sub.get()==''):
        Label(root1,text='please choose valid values',bg='#064134', fg='orange', font=("Comic Sans MS", 15)).place(x=500,y=400)
        return
    riddle=Riddle(filedCombo.get(),sub.get(),w.get())
    riddle.define_riddle()
    num=w.get()
    root1.destroy()
    root=Tk()
    root['background'] = '#064134'
    root.title("write riddle")
    root.geometry("1920x1080")
    title = Label(root, text="Write Riddle", fg='orange',font=("Comic Sans MS", 15), bg='#064134')
    title.place(x=700, y=40)
    text=Text(root, height=10, width=30)
    text.insert(END,'Riddle')
    text.place(x=700, y=100)
    ans_entry=Entry(root)
    ans_entry.insert(0,'Riddle Answer')
    ans_entry.place(x=700,y=300)
    text_exp=Text(root, height=10, width=30)
    text_exp.insert(END,"Riddle Explaination")
    text_exp.place(x=700, y=350)
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addimg.png"))
    resized_image = img.resize((60, 60), Image.ANTIALIAS)
    Addphoto2 = ImageTk.PhotoImage(resized_image)
    img = (Image.open("..//Pictures/reset.png"))
    resized_image = img.resize((80, 50), Image.ANTIALIAS)
    resetimg = ImageTk.PhotoImage(resized_image)
    Label(root, text='Add Riddles By Importing Excel File', bg='#064134', fg='orange',font=("Comic Sans MS", 15)).place(x=220, y=100)
    pathEntry = Entry(root, width=50)
    pathEntry.insert(0, 'file path ')
    pathEntry.place(x=220, y=150)
    sheetEntry = Entry(root, width=50)
    sheetEntry.insert(0, 'sheet name')
    sheetEntry.place(x=220, y=200)

    def home():
        if i < int(num):
            response = messagebox.askyesno("?!", 'activity not completed,do you want to leave?!')
            ##don't wan't to continue activity
            if response == 1:
                currentID = x
                print(x)
                sql = 'DELETE FROM addriddle WHERE id=%s'
                mycursor.execute(sql, (currentID,))
                mydb.commit()
        root.destroy()
        os.system('MainMenu.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(resized_image)
    homebtn = Button(root, image=photo4, command=home, borderwidth=0, bg='#064134')
    homebtn.place(x=20, y=20)
    def delete():
        mylabel.config(text='')
        text.delete("1.0", END)
        ans_entry.delete(0, 'end')
        text_exp.delete("1.0", END)


    def importfile(lb):
        lb.config(text='')
        if not os.path.isfile(pathEntry.get()):
            lb.config(text='please check file format')
            return

        wb = openpyexcel.load_workbook(pathEntry.get())
        if sheetEntry.get() in wb.sheetnames:
         sh = wb[sheetEntry.get()]
         row = sh.max_row
         if (row - 1) > int(num):
             lb.config(text="file contains riddles more than should be!")
             return
         #column = sh.max_column
         for i in range(2, row + 1):
            riddle.addRiddle(sh[i][0].value,sh[i][1].value,sh[i][2].value,Addbtn,resetbtn,importbtn,root)
         lb.config(text='file imported successfully')
        else:
         lb.config(text="sheet doesn't exists")




    lb = Label(root, text='', bg='#064134',wraplength=300, fg='orange',font=("Comic Sans MS", 15))
    lb.place(x=320, y=250)
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/import.png"))
    resized_image = img.resize((80, 70), Image.ANTIALIAS)
    importphoto = ImageTk.PhotoImage(resized_image)
    importbtn = Button(root,image=importphoto,bd=0,bg='#064134',command=lambda :importfile(lb))
    importbtn.place(x=220, y=250)

    Addbtn = Button(root, image=Addphoto2, padx=100, bd=0, bg='#064134',
    command=lambda: riddle.addRiddle(text.get("1.0",END), ans_entry.get(),text_exp.get("1.0",END),Addbtn,resetbtn,importbtn,root))
    resetbtn = Button(root, image=resetimg, command=delete, padx=20, bd=0, bg='#064134')

    resetbtn.place(x=850,y=550)
    Addbtn.place(x=700,y=550)
    mylabel=Label(root,text='',bg='#064134',fg='orange',font=("Comic Sans MS", 15))
    mylabel.place(x=1000,y=350)

    def back():
        root.destroy()
        os.system('riddle.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    #mybtn = Button(root, image=photo, pady=10, padx=20, command=back,bd=0,bg='#064134')
    #mybtn.place(x=20, y=580)
    root.mainloop()

root=Tk()
root['background']='#064134'
root.geometry("1920x1080")
root.title("create riddle")
title=Label(root,text="Create Riddle",bg='#064134', fg='orange',font=("Comic Sans MS", 20))
title.place(x=500,y=40)
vlist=["biology","chemistry","physics","math"]
filedCombo = ttk.Combobox(root, values=vlist)
filedCombo.set("select field")
filedCombo.place(x=570,y=125)
Label(root,text='field',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=120)

sub=Entry(root)
sub.place(x=570,y=185)
Label(root,text='description',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=180)

w = Spinbox(root, from_=1, to=15)
w.place(x=570,y=245)
Label(root,text='riddles number',bg='#064134',fg='orange',font=("Comic Sans MS", 15)).place(x=400,y=240)

Addimg = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addimg.png"))
resized_image = Addimg.resize((90, 80), Image.ANTIALIAS)
Addimg = ImageTk.PhotoImage(resized_image)
addbtn=Button(root,image=Addimg,bd=0,bg='#064134',command=lambda :add_riddle_page(root))
addbtn.place(x=550,y=300)
def back():
    root.destroy()
    os.system('createoptions.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo= ImageTk.PhotoImage(resized_image)
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


