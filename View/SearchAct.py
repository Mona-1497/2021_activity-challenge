
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

#import emoji
import os
import pyttsx3

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mona100%",
    database="ActivityChallengeDB"
 )
if mydb.is_connected():
    db_info=mydb.get_server_info()
    print("connected to mysql server :",db_info)
    print("you're connected")


def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


mycursor = mydb.cursor(buffered=True)
current_user = os.getlogin()


root = Tk()

root.title("Searching For An Activity")
root['background'] = '#064134'

# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1920x1080")
label = Label(root, text='search for an activity',  font=("Comic Sans MS", 20), pady=20, padx=20, bg='#064134', fg='orange')
label.place(x=400,y=15)
searchlb=Label(root, text='', font=20, pady=20, padx=20, bg='#064134')
vList = ["Easy", "Medium", "Hard"]
Combolevel= ttk.Combobox(root, values=vList,width=40)
Combolevel.set("select level")
Combolevel.place(x=400,y=100)
vList=["biology","chemistry","physics","math"]
Combofiled = ttk.Combobox(root, values=vList,width=40)
Combofiled.set("select field")
Combofiled.place(x=400,y=130)
vList=["English","Hebrew","Arabic"]
w = Spinbox(root, from_=1, to=15,width=40)
w.place(x=400,y=160)


def callback4():
    root.destroy()
    os.system('MainMenu.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized_image)
homebtn = Button(root, image=photo5, command=callback4, borderwidth=0, bg='#064134')
homebtn.place(x=20, y=8)
ListAct = Listbox(root, width=70, height=10,bg='#69966d',font=10,fg='#001a00')
ListAct.place(x=200,y=250)
sql="SELECT id,description FROM addactivity WHERE level =%s AND filed=%s AND questionNum=%s  "
sql2 = "SELECT * FROM questions WHERE ActivityID= %s "
#select activity from list

avalb = Label(root, text='', bg='#064134', fg='white', font=("bold", 12))
avalb.place(x=410, y=570)
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/select.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
sel = ImageTk.PhotoImage(resized_image)
def selectAct():
    indexlb.config(text='',image='')
    avalb.config(text='',image='')
    ListAct.delete(0,END)
    level = Combolevel.get()
    filed = Combofiled.get()
    num = w.get()
    mycursor.execute(sql,(level,filed,num))
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        ListAct.insert(END, myresult[i])
    if ListAct.size()>0:
        Button(root, text=' Select and start activity',image=sel,compound=LEFT, bg='#064134', bd=0,font=("bold",12),fg='white', command=select).place(x=400, y=500)

    else:
        avalb.config(text=" Not Available!",image=x,compound=LEFT)

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/ser2.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
serch=ImageTk.PhotoImage(resized_image)
searchBtn = Button(root, image=serch,text="search!",compound=LEFT,font=("bold",12),fg='white', bg='#064134',bd=0,command=selectAct)
searchBtn.place(x=450,y=190)



sql3="SELECT groupName from jointogroup where membername=%s"
sql5="SELECT * FROM sharedAct"

def sharedAct(ActID, groupName ,lb1,lb2):
    lb1.config(text="")
    lb2.config(text="")
    mycursor.execute(sql5,)
    res=mycursor.fetchall()
    for j in range (len(res)):
        if res[j][0]==groupName and res[j][1]==ActID:
           lb1.config(text="activity already shared!")
           return

    mycursor.execute("""INSERT INTO sharedAct (groupName,ActID)
             VALUES (%s, %s)""", (groupName,ActID))
    mydb.commit()
    lb2.config(text="activity shared successfully!")


def share(id, root2):
    root2.destroy()
    root3 = Tk()
    root3.title("share activity with groups")
    root3['background'] = '#064134'
    root3.geometry("1920x1080")
    mycursor.execute(sql3,(current_user,) )
    res = mycursor.fetchall()
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/s2.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    s2 = ImageTk.PhotoImage(resized_image)
    Label(root3,text="Share Activity ",fg='#F39C12',font=("Comic Sans MS", 30),bg='#064134').place(x=450,y=20)
    lb1= Label(root3, text=" ", fg='#F39C12', font=("Comic Sans MS", 15),
                  bg='#064134')
    lb1.place(x=450, y=300)
    lb2=Label(root3,text=" ",fg='#F39C12',font=("Comic Sans MS", 15),bg='#064134')
    lb2.place(x=450,y=300)

    n = StringVar()
    groupchoosen = ttk.Combobox(root3, width=20,textvariable=n)
    groupchoosen.place(x=500,y=150)
    groupchoosen['values']=res
    groupchoosen.insert(0,'choose group')
    shbtn=Button(root3,text=' share',bd=0,fg='white',font=("Comic Sans MS", 15),bg='#064134',image=s2,compound=LEFT,command=lambda:sharedAct(id[0],groupchoosen.get(),lb1,lb2))
    shbtn.place(x=500,y=200)

    def back():
        root3.destroy()
        os.system('options.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(resized_image)
    mybtn = Button(root3, image=photo3, bd=0,bg='#064134', command=back)
    mybtn.place(x=20, y=580)

    def callback5():
        root3.destroy()
        os.system('MainMenu.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    photo5 = ImageTk.PhotoImage(resized_image)
    homebtn = Button(root3, image=photo5, command=callback5, borderwidth=0, bg='#064134')
    homebtn.place(x=20, y=8)
    root3.mainloop()
sql4="SELECT Score From users Where Name=%s"
i = 0
j = 0
def addQuestion(result,root1,question_label,activityID,speakbtn,ans1,ans2,ans3,statelb,correctans,ansimg):

    correctans.config(text='')
    statelb.config(text='')
    question_label.config(text='')
    global i
    i = i + 1
    if i >= len(result):
        root1.destroy()
        root2=Tk()
        root2.title("finish activity")
        root2['background'] = '#064134'
        root2.geometry("1920x1080")
        mycursor.execute(sql4,(current_user,) )
        score = mycursor.fetchall()
        mycursor.execute("""UPDATE users
                             SET Score=%s
                                WHERE Name=%s""", ((score[0][0])+j, current_user))
        mydb.commit()
        Label(root2,text="Your Score Is: "+str(j)+"/"+str(len(result)),font=('bold',15),bg='#064134',fg='yellow',pady=30).place(x=550,y=15)
        img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
        resized_image = img.resize((80, 60), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_image)
        def back1():
            root2.destroy()
            os.system('SearchAndChooseAct.py')
        Button(root2,image=photo,command=back1,bg='#064134',bd=0).place(x=20,y=580)

        img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/fin2.png"))
        resized_image = img.resize((500, 500), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(resized_image)
        Label(root2, image=photo2, bd=0,bg='#064134').place(x=400,y=80)
        img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/sharing.png"))
        resized_image = img.resize((50,50), Image.ANTIALIAS)
        photo3 = ImageTk.PhotoImage(resized_image)
        Button(root2,image=photo3,bd=0,fg='#F39C12',font=("Comic Sans MS", 15),bg='#064134',command=lambda :share(activityID,root2)).place(x=20,y=100)
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

    r = StringVar()
    text=StringVar()
    Label(root1, text='Question Number: ' + str(i + 1)+" Of "+str(len(result)), bg='#064134',font=("Comic Sans MS", 15), fg='#99ffe6',pady=40).place(x=350,y=20)
    question_label.config(text=result[i][1])
    #question_label= Label(frame, text=result[i][1],textvariable=text.get(),fg='#F39C12',bg='#064134',font=10,padx=20)
    #question_label.grid(row=5, column=1)
    #ans1=Radiobutton(frame,text=result[i][2],variable=r,value=result[i][2],bg='#064134',font=10)
    #ans1.grid(row=6,column=1)
    ans1.config(text=result[i][2],variable=r,value=result[i][2])
    ans1.select()
    #ans2=Radiobutton(frame,text=result[i][3],variable=r,value=result[i][3],bg='#064134',font=10)
    #ans2.grid(row=7,column=1)
    ans2.config(text=result[i][3],variable=r,value=result[i][3])
    ans2.select()
    #ans3= Radiobutton(frame,text=result[i][4],variable=r,value=result[i][4],bg='#064134',font=10)
    #ans3.grid(row=8,column=1)
    ans3.config(text=result[i][4],variable=r,value=result[i][4])
    ans3.select()
    def clicked(value):
        btnans["state"]="disabled"
        global j
        #statelb=Label(frame,text=' ',bg='#064134',fg='yellow',font=10)
        #statelb.grid(row=12,column=1)

        correctans.config(text="correct answer is: "+result[i][5])
        if value == result[i][5]:
            statelb.config(text='correct answer',fg='yellow')
            j=j+1

        else:
            statelb.config(text='wrong answer',fg='red')
        #ans1.configure(state=DISABLED)
        #ans2.configure(state=DISABLED)
        #ans3.configure(state=DISABLED)
        ans1.deselect()
        ans2.deselect()
        ans3.deselect()
    def talk():
        engine=pyttsx3.init()
        engine.say(question_label['text'])
        engine.runAndWait()

    speakbtn.bind(talk)

    btnans=Button(root1,text=" answer",image=ansimg,compound=LEFT, bg='#064134',bd=0,fg='white',font=("bold",12),command=lambda: clicked(r.get()))
    btnans.place(x=320,y=430)



img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/x.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
x = ImageTk.PhotoImage(resized_image)
indexlb=Label(root, text='', bg='#064134', fg='white', font=("bold", 12))
indexlb.place(x=410, y=570)
def select():

    indexlb.config(text='',image='')
    avalb.config(text='',image='')
    try:
     #mylabel.config(text=ListAct.get(ANCHOR))
     activity_id = (ListAct.get(ANCHOR)[0],)
     mycursor.execute(sql2, activity_id)
     result = mycursor.fetchall()

     def callback4():
         root.destroy()
         os.system('MainMenu.py')

     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     photo5 = ImageTk.PhotoImage(resized_image)
     homebtn = Button(root, image=photo5, command=callback4, borderwidth=0, bg='#064134')
     homebtn.place(x=20, y=8)
     root.destroy()

     root1 = Tk()
     root1['background'] = '#064134'
     root1.geometry("1920x1080")
     root1.title("questions")
     #frame = Frame(root1,bg='#064134')
     #frame.place(x=400,y=20)
     #addQuestion(frame,result,r)

     r = StringVar()
     text=StringVar()
     Label(root1,text='Question Number: '+str(i+1)+"  Of "+str(len(result)),bg='#064134',font=("Comic Sans MS", 15),fg='#99ffe6',pady=40).place(x=350,y=20)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/quesimg.png"))
     resized_image = img.resize((30, 30), Image.ANTIALIAS)
     quesimg = ImageTk.PhotoImage(resized_image)
     question_label = Label(root1, text=result[i][1],image=quesimg,compound=LEFT,textvariable=text.get(), fg='#F39C12', bg='#064134', font=('bold',15),pady=10,padx=20)
     question_label.place(x=300,y=120)
     ans1 = Radiobutton(root1, text=result[i][2], variable=r, value=result[i][2], bg='#064134',  font=('bold',15),fg='#F39C12')
     ans1.place(x=360,y=180)
     ans1.select()
     ans2 = Radiobutton(root1, text=result[i][3], variable=r, value=result[i][3], bg='#064134',  font=('bold',15),fg='#F39C12')
     ans2.place(x=360,y=220)
     ans2.select()
     ans3 = Radiobutton(root1, text=result[i][4], variable=r, value=result[i][4], bg='#064134',  font=('bold',15),fg='#F39C12')
     ans3.place(x=360,y=260)
     ans3.select()
     statelb = Label(root1, text=' ', bg='#064134', fg='yellow',font=10)
     statelb.place(x=360,y=350)
     correctans=  Label(root1, text=" " , bg='#064134',fg='yellow',font=10)
     correctans.place(x=340,y=380)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/ans.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     ans = ImageTk.PhotoImage(resized_image)
     def clicked(value):
        btnans["state"]="disabled"

        global j
        j=0
        correctans.config(text="correct answer is: " + result[i][5],textvariable=text.get())
        if value == result[i][5]:
            statelb.config(text='correct answer',fg='yellow')
            j=j+1

        else:
            statelb.config(text='wrong answer',fg='red')
     #  ans1.configure(state=DISABLED)
      #  ans2.configure(state=DISABLED)
       # ans3.configure(state=DISABLED)
        ans1.deselect()
        ans2.deselect()
        ans3.deselect()
     btnans = Button(root1, text=" answer",image=ans,compound=LEFT, bg='#064134',fg='white',bd=0,font=("bold",12),command=lambda: clicked(r.get()))
     btnans.place(x=320,y=430)

     def talk():
         engine = pyttsx3.init()
         engine.say(question_label['text'])
         engine.runAndWait()

     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/spell.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     speakimg = ImageTk.PhotoImage(resized_image)
     speakbtn=Button(root1, image=speakimg, command=talk, bg='#064134',bd=0)
     speakbtn.place(x=250,y=120)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/nextbtn.png"))
     resized_image = img.resize((60, 80), Image.ANTIALIAS)
     nextimg = ImageTk.PhotoImage(resized_image)
     btn = Button(root1, image=nextimg,bd=0, bg='#064134',command=lambda: addQuestion(result,root1,question_label,activity_id,speakbtn,ans1,ans2,ans3,statelb,correctans,ans))
     btn.place(x=500,y=425)

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
       indexlb.config(text=" please choose activity",image=x,compound=LEFT)


#mylabel=Label(root,text='',padx=20,bg='#064134')
#mylabel.grid(row=8,column=1)
def back():
    root.destroy()
    os.system('SearchAndChooseAct.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,pady=10,padx=20,command=back,bg='#064134',bd=0)
mybtn.place(x=20,y=580)
root.mainloop()
