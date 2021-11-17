import os
from tkinter import *
import pyttsx3
from PIL import Image, ImageTk
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
current_user = os.getlogin()
root = Tk()
root.title("Search Random Activity")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1920x1080")
lTitle = Label(root, text='Your Random Activity',font=("Comic Sans MS", 20), bg='#064134', fg='orange')
lTitle.place(x=400,y=15)
Lb = Listbox(root, width=70, height=10,bg='#69966d',font=10,fg='#001a00')
Lb.place(x=250 ,y=150)
indexlb=Label(root, text='', bg='#064134', fg='white', font=("bold", 12))
indexlb.place(x=460, y=520)


def callback4():
    root.destroy()
    os.system('MainMenu.py')


img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized_image)
homebtn = Button(root, image=photo5, command=callback4, borderwidth=0, bg='#064134')
homebtn.place(x=20, y=8)
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

    #Button(root1, text='listen to the question', command=talk,bg='#4ED8BE').place(x=260,y=420)
    btnans=Button(root1,text=" answer",image=ansimg,compound=LEFT, bg='#064134',bd=0,fg='white',font=("bold",12),command=lambda: clicked(r.get()))
    btnans.place(x=320,y=430)

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/x.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
x = ImageTk.PhotoImage(resized_image)
def select():
    global i
    i=0
    indexlb.config(text='')
    try:
     activity_id = (Lb.get(ANCHOR)[0],)
     mycursor.execute(sql2, activity_id)
     result = mycursor.fetchall()
     root.destroy()
     root1 = Tk()
     root1['background'] = '#064134'
     root1.geometry("1920x1080")
     root1.title('questions')
     #frame = Frame(root1,bg='#064134')
     #frame.place(x=400,y=20)
     #addQuestion(frame,result,r)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/quesimg.png"))
     resized_image = img.resize((30, 30), Image.ANTIALIAS)
     quesimg = ImageTk.PhotoImage(resized_image)
     r = StringVar()
     text = StringVar()
     Label(root1, text='Question Number: ' + str(i + 1) + "  Of " + str(len(result)), bg='#064134',
           font=("Comic Sans MS", 15),fg='#99ffe6',pady=40).place(x=350,y=20)
     question_label = Label(root1, text=result[i][1],image=quesimg,compound=LEFT, textvariable=text.get(), fg='#F39C12', bg='#064134',font=('bold',15),
                            pady=10, padx=20)
     question_label.place(x=300, y=120)
     ans1 = Radiobutton(root1, text=result[i][2], variable=r, value=result[i][2], bg='#064134', font=('bold',15),fg='#F39C12')
     ans1.place(x=360, y=180)
     ans1.select()
     ans2 = Radiobutton(root1, text=result[i][3], variable=r, value=result[i][3], bg='#064134', font=('bold',15),fg='#F39C12')
     ans2.place(x=360, y=220)
     ans2.select()
     ans3 = Radiobutton(root1, text=result[i][4], variable=r, value=result[i][4], bg='#064134',font=('bold',15),fg='#F39C12')
     ans3.place(x=360, y=260)
     ans3.select()
     statelb = Label(root1, text=' ', bg='#064134', fg='yellow',font=10)
     statelb.place(x=360, y=350)
     correctans = Label(root1, text=" ", bg='#064134', fg='yellow',font=10)
     correctans.place(x=340, y=380)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/ans.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     ans = ImageTk.PhotoImage(resized_image)
     def clicked(value):
         btnans["state"] = "disabled"

         global j
         j = 0
         correctans.config(text="correct answer is: " + result[i][5], textvariable=text.get())
         if value == result[i][5]:
             statelb.config(text='correct answer', fg='yellow')
             j = j + 1

         else:
             statelb.config(text='wrong answer', fg='red')
         #  ans1.configure(state=DISABLED)
         #  ans2.configure(state=DISABLED)
         # ans3.configure(state=DISABLED)
         ans1.deselect()
         ans2.deselect()
         ans3.deselect()

     btnans = Button(root1, text=" answer", image=ans,compound=LEFT, bg='#064134',fg='white',bd=0,font=("bold",12), command=lambda: clicked(r.get()))
     btnans.place(x=320, y=430)

     def talk():
         engine = pyttsx3.init()
         engine.say(question_label['text'])
         engine.runAndWait()

     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/spell.png"))
     resized_image = img.resize((50, 50), Image.ANTIALIAS)
     speakimg = ImageTk.PhotoImage(resized_image)
     speakbtn = Button(root1, image=speakimg, command=talk, bg='#064134', bd=0)
     speakbtn.place(x=250, y=120)
     img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/nextbtn.png"))
     resized_image = img.resize((60, 80), Image.ANTIALIAS)
     nextimg = ImageTk.PhotoImage(resized_image)
     btn = Button(root1, image=nextimg, bd=0, bg='#064134',
                  command=lambda: addQuestion(result, root1, question_label, activity_id, speakbtn, ans1, ans2, ans3,
                                              statelb, correctans,ans))
     btn.place(x=500, y=425)

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
        indexlb.config(text=" please choose activity",image=x,compound=LEFT )


#level 1,2->Easy 3,4->Medium 5 Hard
sql="SELECT level From users Where Name=%s"
mycursor.execute(sql,(current_user,) )
level = mycursor.fetchall()
#level[0][0] level
sql="SELECT id,description FROM addactivity WHERE level =%s "
sql2 = "SELECT * FROM questions WHERE ActivityID= %s "

if level[0][0]==1 or level[0][0]==2:
    mycursor.execute(sql,('Easy',))
    result = mycursor.fetchall()
    for i in range(len(result)):
        Lb.insert(END, result[i])

if level[0][0]==3 or level[0][0]==4:
     mycursor.execute(sql, ('Medium',))
     result = mycursor.fetchall()
     for i in range(len(result)):
         Lb.insert(END, result[i])

if level[0][0]==5:
     mycursor.execute(sql, ('Hard',))
     result = mycursor.fetchall()
     for i in range(len(result)):
        Lb.insert(END, result[i])
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/select.png"))
resized_image = img.resize((50, 50), Image.ANTIALIAS)
sel = ImageTk.PhotoImage(resized_image)
Button(root,text='Select and start activity',image=sel,compound=LEFT, bg='#064134', bd=0,font=("bold",12),fg='white', command=select).place(x=450, y=450)


def back():
    root.destroy()
    os.system('SearchAndChooseAct.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,pady=10,padx=20,command=back,bg='#064134',bd=0)
mybtn.place(x=20,y=580)
root.mainloop()
