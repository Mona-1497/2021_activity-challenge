from time import sleep
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
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
current_user = os.getlogin()

root = Tk()

root.title("Searching For A Riddle")
root['background'] = '#064134'
root.geometry("1000x1000")

root.title("Searching For A Match")
root['background'] = '#064134'
root.geometry("1920x1080")

label = Label(root, text='search for a match', font=("Comic Sans MS", 20), bg='#064134', fg='orange')
label.place(x=400,y=40)
searchlb=Label(root, text='', font=20, pady=20, padx=20, bg='#064134')
vlist =["biology","chemistry","physics","math"]

Combofiled = ttk.Combobox(root, values=vlist)
Combofiled.set("select filed")
Combofiled.place(x=450,y=100)


def callback4():
    root.destroy()
    os.system('MainMenu.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized_image)
homebtn = Button(root, image=photo5, command=callback4, borderwidth=0, bg='#064134')
homebtn.place(x=20, y=8)
sql="SELECT * FROM matches WHERE field=%s"
sql2="SELECT * FROM matching WHERE MatchingID=%s"
avalb = Label(root, text='', bg='#064134', fg='white', font=("bold", 12))
avalb.place(x=410, y=570)
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/select.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
sel = ImageTk.PhotoImage(resized_image)
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/x.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
x = ImageTk.PhotoImage(resized_image)
def selectMatch():
    indexlb.config(text='',image='')
    avalb.config(text='',image='')
    ListMatch.delete(0,END)
    filed = Combofiled.get()
    vals = (filed,)
    mycursor.execute(sql, vals)
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        ListMatch.insert(END, myresult[i])
    if ListMatch.size()>0:
        Button(root,text=' Select and start activity',image=sel,compound=LEFT, bg='#064134', bd=0,font=("bold",12),fg='white', command=select).place(x=400, y=500)

    else:
        avalb.config(text="Not Available!",image=x,compound=LEFT)

indexlb=Label(root, text='', bg='#064134',fg='white', font=("bold", 12))
indexlb.place(x=410, y=570)
sql4="SELECT Score From users Where Name=%s"

def finish(root1,countTry):
    root1.destroy()
    root2 = Tk()
    root2['background'] = '#064134'
    root2.geometry("1920x1080")
    root2.title('finish activity')
    Font4 = ("Comic Sans MS", 30, "bold")
    Label(root2, text="Great Job", font=Font4, fg="orange", bg='#064134', padx=100).place(x=440, y=15)
    Label(root2,text='number of tries is: '+str(countTry)+' times',bg='#064134',fg='orange',font=("Comic Sans MS", 15,"bold")).place(x=500,y=75)
    if countTry<=10:
        mycursor.execute(sql4, (current_user,))
        score = mycursor.fetchall()
        mycursor.execute("""UPDATE users
                                    SET Score=%s
                                       WHERE Name=%s""", ((score[0][0]) + (10-countTry), current_user))
        mydb.commit()
        Label(root2, text="Your Score Is: "+str(10-countTry)+" points", font=("Comic Sans MS", 15,"bold"), bg='#064134',fg='yellow').place(x=500,y=120)
    else:
        Label(root2, text='to many tries,no points:(', font=("Comic Sans MS", 15,"bold"), bg='#064134',fg='yellow').place(x=500,y=120)

    def back1():
        root2.destroy()
        os.system('chooseMatch.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    backph = ImageTk.PhotoImage(resized_image)

    Button(root2, image=backph, command=back1,bg='#064134',bd=0).place(x=20, y=580)

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/fin2.png"))
    resized_image = img.resize((500, 500), Image.ANTIALIAS)
    finish = ImageTk.PhotoImage(resized_image)
    Label(root2, image=finish, bd=0,bg='#064134').place(x=400,y=180)
    def callback4():
        root2.destroy()
        os.system('MainMenu.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(resized_image)
    homebtn = Button(root2, image=photo4, command=callback4, borderwidth=0, bg='#064134')
    homebtn.place(x=20, y=20)
    root2.mainloop()


global flag
flag=False


def select():

    indexlb.config(text='')
    avalb.config(text='')
    try:
     global count, ans_list, ans_dict,countTry
     match_id = (ListMatch.get(ANCHOR)[0],)
     mycursor.execute(sql2, match_id)
     result = mycursor.fetchall()
     root.destroy()

     root1 = Tk()
     root1.geometry("1920x1080")
     root1['background'] = '#064134'
     root1.title("Find Matches")
     title = Label(root1, text="Find Matches", font=("Comic Sans MS", 15), bg='#064134', fg='orange')
     title.pack(pady=10)
     frame = Frame(root1, bg="#064134")
     frame.pack(pady=10)

     def callback4():
         if flag==True:
           response = messagebox.askyesno("?!", 'activity not finished,do you want to leave?!')
           if response==1:
             root1.destroy()
             os.system('MainMenu.py')
         else:
             root1.destroy()
             os.system('MainMenu.py')



     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     photo5 = ImageTk.PhotoImage(resized_image)
     homebtn = Button(root1, image=photo5, command=callback4, borderwidth=0, bg='#064134')
     homebtn.place(x=20, y=8)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/good.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     good = ImageTk.PhotoImage(resized_image)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/notgood.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     notgood = ImageTk.PhotoImage(resized_image)
     img2 = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/fin.png"))
     resized_image = img2.resize((50, 50), Image.ANTIALIAS)
     fin = ImageTk.PhotoImage(resized_image)
     values = []
     for i in range(0, len(result)):
        values.append(result[i][1])
     count = 0
     countTry=0
     ans_list = []
     ans_dict = {}
     lb = Label(root1,bd=0,text='', font=("Comic Sans MS", 15),bg="#064134", fg='yellow')

     random.shuffle(result)
     def clicked(btn, number):
        global count, ans_list, ans_dict,countTry
        if btn["text"] == ' ' and count < 2:
           btn["text"] =result[number][1]
           ans_list.append(number)
           ans_dict[btn] = result[number][1]
           count += 1
           return
        if len(ans_list) == 2:
            if result[ans_list[0]][2] == result[ans_list[1]][2]:
                lb.config(text="match!",fg='#001a00', image=good,compound=LEFT)
                for key in ans_dict:
                    key["state"] = "disabled"

                count = 0
                ans_list = []
                ans_dict = {}
            else:
                lb.config(text="try again!!",fg='red',image=notgood,compound=LEFT)
                count = 0
                countTry+=1
                ans_list = []
                for key in ans_dict:
                    key["text"] = " "
                ans_dict = {}

        for k in range (len(btnlist)):
            if (btnlist[k])["state"]!='disabled':
                global flag
                flag=True


        if flag!=True:
            b1=Button(root1,text='  finish',font=("bold",15),fg='white', image=fin,compound=LEFT,bd=0,pady=10, bg='#064134',command=lambda: finish(root1,countTry))
            b1.pack()


        flag=False

     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/answer.png"))
     resized_image = img.resize((100, 90), Image.ANTIALIAS)
     square = ImageTk.PhotoImage(resized_image)
     btnlist = []
     btn0 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'),command=lambda: clicked(btn0, 0), bg='#064134',bd=0)
     btnlist.append(btn0)
     btn1 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'),  command=lambda: clicked(btn1, 1),bg='#064134',bd=0)
     btnlist.append(btn1)
     btn2 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'), command=lambda: clicked(btn2, 2), bg='#064134',bd=0)
     btnlist.append(btn2)
     btn3 = Button(frame, text=' ', image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'), command=lambda: clicked(btn3, 3), bg='#064134',bd=0)
     btnlist.append(btn3)
     btn4 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'), command=lambda: clicked(btn4, 4), bg='#064134',bd=0)
     btnlist.append(btn4)
     btn5 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'), command=lambda: clicked(btn5, 5), bg='#064134',bd=0)
     btnlist.append(btn5)
     btn6 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'), command=lambda: clicked(btn6, 6), bg='#064134',bd=0)
     btnlist.append(btn6)
     btn7 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'),  command=lambda: clicked(btn7, 7), bg='#064134',bd=0)
     btnlist.append(btn7)
     btn8 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'), command=lambda: clicked(btn8, 8), bg='#064134',bd=0)
     btnlist.append(btn8)
     btn9 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'), command=lambda: clicked(btn9, 9), bg='#064134',bd=0)
     btnlist.append(btn9)
     btn10 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'),  command=lambda: clicked(btn10, 10), bg='#064134',bd=0)
     btn10["state"] = "disabled"
     btn11 = Button(frame, text=' ',image=square,compound=CENTER,font=("Comic Sans MS", 10,'bold'), command=lambda: clicked(btn11, 11), bg='#064134',bd=0)
     btn11["state"] = "disabled"

     btn0.grid(row=0, column=0)
     btn1.grid(row=0, column=1)
     btn2.grid(row=0, column=2)
     btn3.grid(row=1, column=0)
     btn4.grid(row=1, column=1)
     btn5.grid(row=1, column=2)
     btn6.grid(row=2, column=0)
     btn7.grid(row=2, column=1)
     btn8.grid(row=2, column=2)
     btn9.grid(row=3, column=0)
     btn10.grid(row=3, column=1)
     btn11.grid(row=3, column=2)
     lb.pack(pady=10)


     def back():
        root1.destroy()
        os.system('chooseMatch.py')

     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
     resized_image = img.resize((80, 60), Image.ANTIALIAS)
     photo = ImageTk.PhotoImage(resized_image)
     mybtn = Button(root1, image=photo, pady=10, padx=20, command=back,bg='#064134',bd=0)
     mybtn.place(x=20, y=580)
     root1.mainloop()
    except:
       indexlb.config(text=" please choose match",image=x,compound=LEFT)

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/ser2.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
serch=ImageTk.PhotoImage(resized_image)
searchBtn = Button(root,image=serch, text="search!",compound=LEFT,font=("bold",12),fg='white', bg='#064134',bd=0,command=selectMatch)
searchBtn.place(x=450,y=150)

#mybtn=Button(root,text='Select and Start Match',bg='#F39C12',pady=10,padx=20,command=select)
#mybtn.place(x=330,y=430)
def back():
    root.destroy()
    os.system('options.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)

mybtn=Button(root,image=photo,pady=10,padx=20,command=back,bg='#064134',bd=0)
mybtn.place(x=20,y=580)
ListMatch = Listbox(root, width=70, height=10,bg='#69966d',font=10,fg='#001a00')
ListMatch.place(x=200,y=240)


root.mainloop()