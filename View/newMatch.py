from tkinter import *
from tkinter import ttk, messagebox
import os
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
class Match():
    def __init__(self, field, description):
        self.field = field
        self.description = description
        self.currentID = 0
        self.matches = []


    def define_match(self):
        mycursor.execute("""INSERT INTO matches(field,description)
                                VALUES (%s, %s)""", (self.field, self.description))
        global x1
        x1= mycursor.lastrowid
        self.currentID = x1
        mydb.commit()


    def addmatch(self,value,matchTo,Addbtn,resbtn,root):
        global i
        i=i+1
        if i <= 10:

         self.matches.append({value: matchTo})
         x = []
         try:
          for key, values in self.matches[len(self.matches) - 1].items():
            x.append(key)
            x.append(values[0])
            mycursor.execute("""
                              INSERT INTO matching(MatchingID,value,ismachTo)
                              VALUES (%s,%s, %s)""", (self.currentID, x[0], x[1]))
          mydb.commit()
          mylabel.config(text="card "+str(i)+" inserted")
         except:
            i=i-1
            mylabel.config(text="please,insert valid values")

         if i==10:
             Addbtn.place_forget()
             resbtn.place_forget()
             mylabel.config(text="Match Is Completed")




def add_match_page(root):
    global mylabel
    if (filedCombo.get() == 'select field') or (description.get("1.0",END)=='\n'):
        Label(root, text='please choose valid values', bg='#064134', fg='orange', font=("Comic Sans MS", 15)).place(x=550, y=450)
        return
    match=Match(filedCombo.get(),description.get("1.0",END))
    match.define_match()
    root.destroy()
    root1=Tk()
    root1['background'] = '#064134'
    root1.geometry("1920x1080")
    root1.title("match cards")
    title = Label(root1, text="Match Cards", fg='orange',font=("Comic Sans MS", 15), bg='#064134')
    title.place(x=550, y=40)
    firstcard=Label(root1,text='vlaue',fg='orange',font=("Comic Sans MS", 15),bg='#064134')
    firstcard.place(x=450,y=120)
    e1=Entry(root1)
    e1.place(x=450,y=160)
    secondcard = Label(root1, text='matching to',fg='orange',font=("Comic Sans MS", 15), bg='#064134')
    secondcard.place(x=650, y=120)
    e2= Entry(root1)
    e2.place(x=650, y=160)

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addimg.png"))
    resized_image = img.resize((60, 60), Image.ANTIALIAS)
    Addphoto2 = ImageTk.PhotoImage(resized_image)
    for i in range(0,10):
        Addbtn = Button(root1, image=Addphoto2, padx=100, bd=0, bg='#064134',command=lambda: match.addmatch(e1.get(),e2.get(),Addbtn,reybtn,root1))

    Addbtn.place(x=450,y=240)
    mylabel=Label(root1,text='',font=("Comic Sans MS", 12),fg='orange',bg='#064134')
    mylabel.place(x=450,y=320)

    def back():
        root1.destroy()
        os.system('newMatch.py')
    def delete():
        mylabel.config(text='')
        e1.delete(0,'end')
        e2.delete(0,'end')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    mybtn = Button(root1, image=photo,  pady=10, padx=20, command=back,bg='#064134',bd=0)
    mybtn.place(x=20, y=580)

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/reset.png"))
    resized_image = img.resize((80, 50), Image.ANTIALIAS)
    resphoto = ImageTk.PhotoImage(resized_image)
    reybtn = Button(root1,image=resphoto,padx=20,command=delete,bg='#064134',bd=0)
    reybtn.place(x=580,y=240)

    def home():
        if i < 10:
            response = messagebox.askyesno("?!", 'activity not completed,do you want to leave?!')
            ##don't wan't to continue activity
            if response == 1:
                currentID = x1
                sql = 'DELETE FROM matches WHERE id=%s'
                mycursor.execute(sql, (currentID,))
                mydb.commit()

        root1.destroy()
        os.system('MainMenu.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(resized_image)
    homebtn = Button(root1, image=photo4, command=home, borderwidth=0, bg='#064134')
    homebtn.place(x=20, y=20)

    root1.mainloop()

root=Tk()
root['background']='#064134'
root.geometry("1920x1080")
root.title("create match")
title=Label(root,text="Create Match",fg='orange',font=("Comic Sans MS", 20),bg='#064134')
title.place(x=550,y=40)
vlist=["biology","chemistry","physics",'math']
filedCombo = ttk.Combobox(root, values=vlist)
filedCombo.set("select field")
filedCombo.place(x=550,y=120)
Label(root,text="Match Description: ",bg='#064134',font=("Comic Sans MS", 15, ),fg="orange").place(x=550,y=160)
description=Text(root,width=20,height=5)
description.place(x=550,y=200)
#Addimg = PhotoImage(file = "../View/Pictures/Add.png")
Addimg = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addimg.png"))
resized_image = Addimg.resize((90, 80), Image.ANTIALIAS)
Addimg = ImageTk.PhotoImage(resized_image)
addbtn=Button(root,image=Addimg,bd=0,bg='#064134',command=lambda :add_match_page(root))
addbtn.place(x=550,y=350)
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