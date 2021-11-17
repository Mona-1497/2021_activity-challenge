from tkinter import *

import pyttsx3
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
#import emoji
import os
import random

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

root = Tk()

root.title("Searching For A Riddle")
root['background'] = '#064134'
root.geometry("1920x1080")

label = Label(root, text='search for a riddle', font=("Comic Sans MS", 20), bg='#064134', fg='orange')
label.place(x=400,y=40)
#searchlb=Label(root, text='', font=20, pady=20, padx=20, bg='#064134')
vlist =["biology","chemistry","physics","math"]

Combofiled = ttk.Combobox(root, values=vlist)
Combofiled.set("select field")
Combofiled.place(x=450,y=100)
w = Spinbox(root, from_=1, to=15)
w.place(x=450,y=140)

def callback4():
    root.destroy()
    os.system('MainMenu.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized_image)
homebtn = Button(root, image=photo5, command=callback4, bd=0, bg='#064134')
homebtn.place(x=20, y=8)
ListRiddle = Listbox(root, width=70, height=10,bg='#69966d',font=10,fg='#001a00')
ListRiddle.place(x=200,y=250)
sql="SELECT * FROM addRiddle WHERE filed=%s and riddlesNum=%s "
sql2= "SELECT * FROM riddle WHERE RiddleID= %s "
sql3= "SELECT answer FROM riddle WHERE RiddleID= %s "

avalb = Label(root, text='', bg='#064134', fg='white', font=("bold", 12))
avalb.place(x=410, y=570)
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/select.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
sel = ImageTk.PhotoImage(resized_image)
def selectRiddle():
    indexlb.config(text='',image='')
    avalb.config(text='',image='')
    ListRiddle.delete(0,END)
    filed = Combofiled.get()
    num = w.get()
    vals=(filed,num)
    mycursor.execute(sql,vals)
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        ListRiddle.insert(END, myresult[i])

    if ListRiddle.size()>0:
        Button(root, text='Select and start activity',image=sel,compound=LEFT, bg='#064134', bd=0,font=("bold",12),fg='white', command=select).place(x=400, y=500)

    else:
        avalb.config(text=' Not Available!',image=x,compound=LEFT)

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/ser2.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
serch=ImageTk.PhotoImage(resized_image)
searchBtn = Button(root, image=serch, text="search!",compound=LEFT,font=("bold",12),fg='white', bg='#064134',bd=0,command=selectRiddle)
searchBtn.place(x=450,y=180)
i=0
j=0

def again(root1,riddlebtn,result,label,speakbtn,speakbtn2,c):
    riddlebtn["state"] = "active"
    speakbtn["bg"]='#064134'
    c.config(text='')
    speakbtn2.place_forget()

    global i
    i = i + 1
    if i >= len(result):
        root1.destroy()
        root2 = Tk()
        root2.title("finish activity")
        root2['background'] = '#064134'
        root2.geometry("1920x1080")
        Label(root2,text="Your Score Is: "+str(j)+"/"+str(len(result)),font=('bold',15),bg='#064134',fg='yellow',pady=30).place(x=550,y=20)

        img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
        resized_image = img.resize((80, 60), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_image)

        def back1():
            root2.destroy()
            os.system('chooseRiddle.py')
        Button(root2, image=photo, command=back1,bg='#064134',bd=0).place(x=20, y=580)

        img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/fin2.png"))
        resized_image = img.resize((500, 500), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(resized_image)
        Label(root2, image=photo2, bd=0,bg='#064134').place(x=400,y=80)
        #Button(root2,text='share with group').place(x=800,y=200)
        def callback4():
            root2.destroy()
            os.system('MainMenu.py')

        img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
        resized_image = img.resize((50, 50), Image.ANTIALIAS)
        photo4 = ImageTk.PhotoImage(resized_image)
        homebtn = Button(root2, image=photo4, command=callback4, borderwidth=0, bg='#064134')
        homebtn.place(x=20, y=20)
        root2.mainloop()

        return
    label.place_forget()
    #riddlebtn["state"]="active"
    #riddlebtn["bg"]= '#4ED8BE'
    #my_label.place_forget()

    def clicked(btn):
        #global my_label
        global j
        speakbtn2.place(x=580, y=500)
        btn["text"] = result[i][2]
        #tn["fg"] = "orange"
        #btn["state"]="disabled"
        #my_label = Label(frame, width=20, heigh=10, text=result[i][3], wraplength=80, justify=CENTER)
        #my_label.place(x=500, y=200)
        label.place(x=580, y=240)
        label.config(text=result[i][3])
       # speakbtn.config(text='listen to answer')
        if result[i][2] ==answers.get():
            c.config( text='correct answer ' , bg='#064134',
                  fg='white', font=('bold',12))

            j=j+1


        else:
            c.config( text='wrong answer' , bg='#064134', fg='red', font=('bold',12))

    def talk():
         engine = pyttsx3.init()
         engine.say(riddlebtn['text'])
         engine.runAndWait()
    speakbtn['command']=talk
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/square.png"))
    resized_image = img.resize((250, 255), Image.ANTIALIAS)
    square2 = ImageTk.PhotoImage(resized_image)
   #btn1 = Button(root1, text=result[i][1], wraplength=80, image=square2,bd=0,compound=CENTER, bg='#064134', command=lambda: clicked(btn1))
    #btn1.place(x=300, y=250)
    riddlebtn.config(text=result[i][1])
    riddlebtn.config(command=lambda: clicked(riddlebtn))



img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/x.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
x = ImageTk.PhotoImage(resized_image)
indexlb=Label(root, text='', bg='#064134', fg='white', font=("bold", 12))
indexlb.place(x=410, y=570)
def select():

    indexlb.config(text='',image='')
    avalb.config(text='',image='')
    try:
     global answers
     #mylabel.config(text=ListRiddle.get(ANCHOR))
     riddle_id = (ListRiddle.get(ANCHOR)[0],)
     mycursor.execute(sql2, riddle_id)
     result = mycursor.fetchall()
     root.destroy()
     root1 = Tk()
     root1.title("guess riddle")
     root1['background'] = '#064134'
     root1.geometry("1920x1080")
     title=Label(root1,text="GUESS ME!!",font=("Comic Sans MS", 20),fg='orange',bg= '#064134')
     title.place(x=500,y=20)

     mycursor.execute(sql3, riddle_id)
     resultans=mycursor.fetchall()
     vlist2 = []
     for k in range(0, len(resultans)):
        vlist2.insert(k, resultans[k][0])
     vlist2 = list(dict.fromkeys(vlist2))
     random.shuffle(vlist2)
     answers = ttk.Combobox(root1, values=vlist2)
     answers.set("select answer ")
     answers.place(x=400, y=150)
     c = Label(root1, text='', bg='#064134', fg='yellow', font=10)
     c.place(x=580, y=148)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/square.png"))
     resized_image = img.resize((250, 255), Image.ANTIALIAS)
     ans = ImageTk.PhotoImage(resized_image)

     def talk():
         engine = pyttsx3.init()
         engine.say(btn1['text'])
         engine.runAndWait()
     def talk2():
         engine = pyttsx3.init()
         engine.say(result[i][3])
         engine.runAndWait()
     def clicked(btn1):
        global my_label
        global j
        #show correct answer
        btn1["text"] = result[i][2]
        #btn["bg"]="orange"
        #btn["state"]="disabled"
        #riddle explaination
        my_label=Label(root1,image=ans,bd=0,bg='#064134',compound=CENTER,text=result[i][3],wraplength=80, justify=CENTER)
        my_label.place(x=580,y=240)
        btn.place(x=900, y=320)




        #speakbtn2 = Button(frame, image=speakimg, command=talk2,bg='#064134', bd=0)
        speakbtn2.place(x=580, y=500)
        #speakbtn.config(text='listen to answer')

        if result[i][2]==answers.get():
           c.config(text='correct answer',bg='#064134',fg='white',font=('bold',12))
           j=j+1
        else:
            c.config(text='wrong answer',bg='#064134',fg='red',font=('bold',12))


     #riddle content
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/square.png"))
     resized_image = img.resize((250,255), Image.ANTIALIAS)
     square = ImageTk.PhotoImage(resized_image)
     btn1=Button(root1,text=result[i][1], wraplength=80, image=square,compound=CENTER,bd=0,bg='#064134',command=lambda :clicked(btn1))
     btn1.place(x=300,y=240)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/spell.png"))
     resized_image = img.resize((30, 30), Image.ANTIALIAS)
     speakimg = ImageTk.PhotoImage(resized_image)
     speakbtn = Button(root1, image=speakimg, command=talk, bg='#064134', bd=0)
     speakbtn.place(x=300, y=500)
     speakbtn2 = Button(root1, image=speakimg, command=talk2, bg='#064134', bd=0)

     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/nextbtn.png"))
     resized_image = img.resize((60, 80), Image.ANTIALIAS)
     nextimg = ImageTk.PhotoImage(resized_image)
     btn = Button(root1, image=nextimg,bd=0,bg='#064134', command=lambda: again(root1,btn1, result,my_label,speakbtn,speakbtn2,c))
     #btn.place(x=900,y=320)

     def callback4():
         root1.destroy()
         os.system('MainMenu.py')

     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     photo5 = ImageTk.PhotoImage(resized_image)
     homebtn = Button(root1, image=photo5, command=callback4, borderwidth=0, bg='#064134')
     homebtn.place(x=20, y=8)
     root1.mainloop()
    except:
        indexlb.config(text=" please choose riddle",image=x,compound=LEFT)



def back():
    root.destroy()
    os.system('options.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,pady=10,padx=20,command=back,bg='#064134',bd=0)
mybtn.place(x=20,y=580)
#mylabel=Label(root,text='',padx=20,bg='#064134')
#mylabel.grid(row=9,column=1)

root.mainloop()
