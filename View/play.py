import os
from random import random
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk,Image
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





root=Tk()
root['background']='#064134'
root.geometry("1920x1080")
root.title("search classification")
vlist =["biology","chemistry","physics","math"]
Combofiled = ttk.Combobox(root, values=vlist)
Combofiled.set("select field")
Combofiled.place(x=450,y=100)
w = Spinbox(root, from_=1, to=15)
w.place(x=450,y=150)
List = Listbox(root, width=70, height=10,bg='#69966d',font=10,fg='#001a00')
List.place(x=200,y=250)


def callback4():
    root.destroy()
    os.system('MainMenu.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized_image)
homebtn = Button(root, image=photo5, command=callback4, borderwidth=0, bg='#064134')
homebtn.place(x=20, y=8)


sql="SELECT * FROM Classification WHERE filed=%s AND CardsNum=%s"
sql2="SELECT * FROM answers WHERE classificationid=%s"

list1=[]
list2=[]
x=0
indexlb=Label(root, text='', bg='#064134', fg='white', font=("bold", 12))
indexlb.place(x=410, y=570)
def start():
    indexlb.config(text='')
    avalb.config(text='')
    global list1, list2, x, flag
    flag = False

    def checkLists():
        listcol1=[]
        listcol2=[]
        for i in range (0,len(result)):
            if result[i][1]==column1:
                listcol1.append(result[i][2])
        for i in range (0,len(result)):
            if result[i][1]==column2:
                listcol2.append(result[i][2])

        if list1==listcol1 and list2 == listcol2:
           root1.destroy()
           root2=Tk()
           root2['background'] = '#064134'
           root2.geometry("1920x1080")
           root2.title('finish activity')
           Font4 = ("Comic Sans MS", 30, "bold")

           Label(root2,text="Great Job",font=Font4,fg="orange",bg='#064134',padx=100).place(x=450,y=20)

           Label(root2,text=column1+':' ,font=("Comic Sans MS", 12),fg="orange",bg='#064134').place(x=100,y=80)
           Label(root2,text=listcol1,font=("Comic Sans MS", 12),fg="orange",bg='#064134').place(x=120,y=120)
           Label(root2, text=column2 + ':', font=("Comic Sans MS", 12), fg="orange", bg='#064134').place(x=100, y=160)
           Label(root2, text=listcol2, font=("Comic Sans MS", 12), fg="orange", bg='#064134').place(x=120, y=200)

           def back1():
               root2.destroy()
               os.system('play.py')

           img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
           resized_image = img.resize((80,60), Image.ANTIALIAS)
           backph = ImageTk.PhotoImage(resized_image)

           Button(root2, image=backph,  command=back1,bg='#064134',bd=0).place(x=20, y=580)

           img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/fin2.png"))
           resized_image = img.resize((500, 500), Image.ANTIALIAS)
           finish = ImageTk.PhotoImage(resized_image)
           Label(root2, image=finish, bd=0,bg='#064134').place(x=400,y=80)

           def callback4():
               root2.destroy()
               os.system('MainMenu.py')

           img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
           resized_image = img.resize((50, 50), Image.ANTIALIAS)
           photo4 = ImageTk.PhotoImage(resized_image)
           homebtn = Button(root2, image=photo4, command=callback4, borderwidth=0, bg='#064134')
           homebtn.place(x=20, y=20)
           root2.mainloop()


        else:
            root1.destroy()
            root2 = Tk()
            root2['background'] = '#064134'
            root2.geometry("1920x1080")
            root2.title('finish activity')
            Font4 = ("Comic Sans MS", 30, "bold")

            Label(root2, text="Try Again!", font=Font4, fg="orange", bg='#064134', padx=100).place(x=450, y=20)
            Label(root2, text=column1 + ':', font=("Comic Sans MS", 12), fg="orange", bg='#064134').place(x=100, y=80)
            Label(root2, text=listcol1, font=("Comic Sans MS", 12), fg="orange", bg='#064134').place(x=120, y=120)
            Label(root2, text=column2 + ':', font=("Comic Sans MS", 12), fg="orange", bg='#064134').place(x=100, y=160)
            Label(root2, text=listcol2, font=("Comic Sans MS", 12), fg="orange", bg='#064134').place(x=120, y=200)

            img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/bb.png"))
            resized_image = img.resize((80, 50), Image.ANTIALIAS)
            backph = ImageTk.PhotoImage(resized_image)


            img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/fin2.png"))
            resized_image = img.resize((500, 500), Image.ANTIALIAS)
            finish = ImageTk.PhotoImage(resized_image)
            Label(root2, image=finish, bd=0,bg='#064134').place(x=400,y=80)

            def back1():

             root2.destroy()
             os.system('play.py')

            img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
            resized_image = img.resize((80, 60), Image.ANTIALIAS)
            backph = ImageTk.PhotoImage(resized_image)

            Button(root2, image=backph, command=back1,bg='#064134',bd=0).place(x=20, y=580)

            def callback4():
                root2.destroy()
                os.system('MainMenu.py')

            img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
            resized_image = img.resize((50, 50), Image.ANTIALIAS)
            photo4 = ImageTk.PhotoImage(resized_image)
            homebtn = Button(root2, image=photo4, command=callback4, borderwidth=0, bg='#064134')
            homebtn.place(x=20, y=20)
            root2.mainloop()
            root2.mainloop()


    def end_x(event):
        widget = event.widget
        x = widget.winfo_x()
        l3.unbind("<B1-Motion>")
        l3.unbind("<Button-1>")
        l3.unbind("<ButtonRelease>")
        if x > 200 and x < 575:
            list1.append(l3.cget("text"))
            print(l3["text"])

        if x > 575 and x < 950:
            list2.append(l3.cget("text"))
            print(l3["text"])
        global flag
        flag = True
        return

    def drag_start(event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y
        return

    def drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)
        return

    try:

     column1=List.get(ANCHOR)[3]
     column2=List.get(ANCHOR)[4]
     classify_id = (List.get(ANCHOR)[0],)
     mycursor.execute(sql2, classify_id)
     result = mycursor.fetchall()
     random.shuffle(result)
     root.destroy()
     root1=Tk()
     root1['background'] = '#064134'
     root1.geometry("1920x1080")
     root1.title("classify cards")
     my_canvas = Canvas(root1, width=375, height=400, bg='#064134')
     my_canvas2 = Canvas(root1, width=375, height=400, bg='#064134')
     my_canvas.place(x=200, y=100)
     my_canvas2.place(x=575, y=100)
     Font1 = ("Comic Sans MS", 30)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/cl.png"))
     resized_image = img.resize((300, 105), Image.ANTIALIAS)
     cl = ImageTk.PhotoImage(resized_image)
     l1 = Label(root1, text=column1, image=cl,compound=CENTER, fg='#064134', font=Font1,bg='#064134')
     l1.place(x=250, y=105)
     l2 = Label(root1, text=column2,image=cl,compound=CENTER, fg='#064134', font=Font1,bg='#064134')
     l2.place(x=640, y=105)
     Font3 = ("Comic Sans MS", 30)
     Label(root1,text="Classify",font=Font3,fg='orange',bg='#064134').place(x=500,y=20)
     global finished
     finished=0
     def callback4():
         if finished==0:
           response = messagebox.askyesno("?!", 'activity not finished,do you want to leave?!')
           if response == 1:
             root1.destroy()
             os.system('MainMenu.py')
         else:
             root1.destroy()
             os.system('MainMenu.py')


     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     photohome = ImageTk.PhotoImage(resized_image)
     homebtn2 = Button(root1, image=photohome, command=callback4, borderwidth=0, bg='#064134')
     homebtn2.place(x=20, y=8)
     root1.update()
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/square.png"))
     resized_image = img.resize((70, 70), Image.ANTIALIAS)
     square = ImageTk.PhotoImage(resized_image)
     for i in range(0,len(result)):
       flag = False
       l3 = Label(root1, text=result[i][2],image=square,compound=CENTER,bd=0,bg= '#064134', font=15)
       l3.place(x=1000, y=300)
       l3.config(text=result[i][2])
       l3.bind("<Button-1>", drag_start)
       root1.update()
       l3.bind("<B1-Motion>", drag_motion)
       l3.bind("<ButtonRelease>", end_x)
       while flag != True:
           root1.update()
     finished=1
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/fin.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     fin = ImageTk.PhotoImage(resized_image)
     finish = Button(root1,text='  finish',font=("bold",15),fg='white', image=fin,compound=LEFT,bd=0, bg='#064134',command=checkLists)
     finish.place(x=500, y=550)
     root1.mainloop()


    except:
       indexlb.config(text="please choose classification",image=x,compound=LEFT)



avalb = Label(root, text='', bg='#064134', fg='white', font=("bold", 12))
avalb.place(x=410, y=570)
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/select.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
sel = ImageTk.PhotoImage(resized_image)
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/x.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
x = ImageTk.PhotoImage(resized_image)
def select():
    indexlb.config(text='',image='')
    avalb.config(text='',image='')
    List.delete(0,END)
    filed = Combofiled.get()
    mycursor.execute(sql, (filed,w.get()))
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        List.insert(END, myresult[i])
    if List.size()>0:

        Button(root, text=' Select and Start Activity',image=sel,compound=LEFT, bg='#064134', bd=0,font=("bold",12),fg='white', command=start).place(x=400, y=500)

    else:
       avalb.config(text=" Not Available!",image=x,compound=LEFT)



img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/ser2.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
serch=ImageTk.PhotoImage(resized_image)

Button(root,image=serch, text="search!",compound=LEFT,font=("bold",12),fg='white', bg='#064134',bd=0,command=select).place(x=450,y=180)
Label(root,text="search classification", font=("Comic Sans MS",20), bg='#064134', fg='orange').place(x=400,y=40)
def back():
    root.destroy()
    os.system('options.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,pady=10,padx=20,command=back,bd=0,bg='#064134')
mybtn.place(x=20,y=580)
root.mainloop()