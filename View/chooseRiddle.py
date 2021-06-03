from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import emoji
import os
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
root.geometry("1000x1000")

label = Label(root, text='search for a riddle', font=20, pady=20, padx=20, bg='#064134', fg='white')
label.grid(row=1, column=1)
searchlb=Label(root, text='', font=20, pady=20, padx=20, bg='#064134')
vlist =["biology","chemistry","physics","math"]

Combofiled = ttk.Combobox(root, values=vlist)
Combofiled.set("select filed")
Combofiled.grid(row=3, column=1, ipadx=10)


ListRiddle = Listbox(root, width=70, height=10,bg='#69966d',font=10,fg='yellow')
ListRiddle.grid(row=6, column=1)
sql="SELECT * FROM addRiddle WHERE filed=%s "
sql2= "SELECT * FROM riddle WHERE RiddleID= %s "
sql3= "SELECT answer FROM riddle WHERE RiddleID= %s "


def selectRiddle():

    filed = Combofiled.get()
    vals=(filed,)
    mycursor.execute(sql,vals)
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        ListRiddle.insert(END, myresult[i])

searchBtn = Button(root, text='Search', bg='#69966d', font=30, width=10,command=selectRiddle)
searchBtn.grid(row=5, column=1, pady=20)
i=0
j=0

def again(frame,result,root1,label):


    global i
    i = i + 1
    if i >= len(result):
        root1.destroy()
        root2 = Tk()
        root2.title("finish activity")
        root2['background'] = '#064134'
        root2.geometry("1000x1000")

        def back():
            root2.destroy()
            os.system('options.py')

        photo = PhotoImage(file="../View/Pictures/back.png")
        mybtn = Button(root2, image=photo, bg='#F39C12', pady=10, padx=20, command=back)
        mybtn.place(x=300, y=200)
        root2.mainloop()

        return
    label.place_forget()
    my_label.place_forget()

    def clicked(btn):
        global my_label

        btn["text"] = result[i][2]
        btn["bg"] = "orange"
        btn["state"]="disabled"
        my_label = Label(frame, width=20, heigh=10, text=result[i][3], wraplength=80, justify=CENTER)
        my_label.place(x=500, y=100)
        if result[i][2] ==answers.get():
            c=Label(frame, text='correct answer ' + emoji.emojize(":grinning_face_with_big_eyes:"), bg='#064134',
                  fg='yellow', font=10)
            c.place(x=350, y=55)


        else:
            w=Label(frame, text='wrong answer' + emoji.emojize(":thinking_face:"), bg='#064134', fg='red', font=10)
            w.place(x=350, y=55)


    btn1 = Button(frame, text=result[i][1], wraplength=80, justify=CENTER, width=20, height=10, bg='#4ED8BE',
                  command=lambda: clicked(btn1))
    btn1.place(x=300, y=100)

def select():
    global answers
    mylabel.config(text=ListRiddle.get(ANCHOR))
    riddle_id = (ListRiddle.get(ANCHOR)[0],)
    mycursor.execute(sql2, riddle_id)
    result = mycursor.fetchall()
    root.destroy()
    root1 = Tk()
    root1.title("play activity")
    root1['background'] = '#69966d'
    root1.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
    root1.geometry("1000x1000")
    title=Label(root1,text="GUESS ME!!",font=40,fg='yellow',bg='#064134')
    title.place(x=430,y=20)
    frame = Frame(root1,bg='#064134',height=500,width=1500)
    frame.place(x=0,y=100)
    mycursor.execute(sql3, riddle_id)
    resultans=mycursor.fetchall()
    vlist2 = []
    for k in range(0, len(resultans)):
        vlist2.insert(k, resultans[k][0])
    answers = ttk.Combobox(frame, values=vlist2)
    answers.set("select answer ")
    answers.place(x=200, y=55)
    def clicked(btn):
        global my_label
        global j
        btn["text"] = result[i][2]
        btn["bg"]="orange"
        btn["state"]="disabled"
        my_label=Label(frame,width=20,heigh=10,text=result[i][3],wraplength=80, justify=CENTER)
        my_label.place(x=500,y=100)
        if result[i][2]==answers.get():
           c= Label(frame,text='correct answer '+emoji.emojize(":grinning_face_with_big_eyes:"),bg='#064134',fg='yellow',font=10)
           c.place(x=350,y=55)
        else:
            w=Label(frame,text='wrong answer'+emoji.emojize(":thinking_face:"),bg='#064134',fg='red',font=10)
            w.place(x=350,y=55)


    btn1=Button(frame,text=result[i][1], wraplength=80, justify=CENTER,width=20,height=10,bg='#4ED8BE',command=lambda :clicked(btn1))
    btn1.place(x=300,y=100)

    next = PhotoImage(file="../View/Pictures/next.png")
    btn = Button(frame, image=next,bd=0, command=lambda: again(frame, result,root1,my_label))
    btn.place(x=350,y=300)
    root1.mainloop()

mybtn=Button(root,text='Select and Start Riddle',bg='#F39C12',pady=10,padx=20,command=select)
mybtn.grid(row=7,column=1,pady=20)

def back():
    root.destroy()
    os.system('options.py')
photo = PhotoImage(file="../View/Pictures/back.png")
mybtn=Button(root,image=photo,bg='#F39C12',pady=10,padx=20,command=back)
mybtn.grid(row=8,column=1,pady=20)
mylabel=Label(root,text='',padx=20,bg='#064134')
mylabel.grid(row=9,column=1)

root.mainloop()
