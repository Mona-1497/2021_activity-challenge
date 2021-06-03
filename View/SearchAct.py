from tkinter import *
from PIL import Image, ImageTk
import webbrowser
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

root.title("Searching For An Activity")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
label = Label(root, text='search for an activity', font=20, pady=20, padx=20, bg='#064134', fg='white')
label.grid(row=1, column=1)
searchlb=Label(root, text='', font=20, pady=20, padx=20, bg='#064134')
vList = ["Easy", "Medium", "Hard"]
Combolevel= ttk.Combobox(root, values=vList)
Combolevel.set("select level")
Combolevel.grid(row=2, column=1, ipadx=10)
vList=["science","math"]
Combofiled = ttk.Combobox(root, values=vList)
Combofiled.set("select field")
Combofiled.grid(row=3, column=1, ipadx=10)
vList=["English","Hebrew","Arabic"]
Combolan = ttk.Combobox(root, values=vList)
Combolan.set("select language")
Combolan.grid(row=4, column=1, ipadx=10)

ListAct = Listbox(root, width=70, height=10,bg='#69966d',font=10,fg='yellow')
ListAct.grid(row=6, column=1)
sql="SELECT * FROM addactivity WHERE level =%s AND filed=%s AND language=%s  "
sql2 = "SELECT * FROM questions WHERE ActivityID= %s "
#select activity from list


def selectAct():

    level = Combolevel.get()
    filed = Combofiled.get()
    lan = Combolan.get()
    mycursor.execute(sql,(level,filed,lan))
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        ListAct.insert(END, myresult[i])

searchBtn = Button(root, text='Search', bg='#69966d', font=30, width=10,command=selectAct)
searchBtn.grid(row=5, column=1, pady=20)
#select Button
i = 0
j = 0
def addQuestion(frame,result,root1):

    global i
    i = i + 1
    if i >= len(result):
        root1.destroy()
        root2=Tk()
        root2.title("finish activity")
        root2['background'] = '#064134'
        root2.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
        root2.geometry("1000x1000")
        Label(root2,text="Your Score Is: "+str(j)+"/"+str(len(result)),font=20,bg='#064134',fg='yellow',pady=30).place(x=650,y=100)
        Button(root2,text="back to choose activity",bg='#F39C12').place(x=650,y=200)

        def back():
            root2.destroy()
            os.system('MainMenu.py')
        Button(root2,text="back to mainmenu",bg='#F39C12',command=back).place(x=650,y=250)
        finishPhoto = PhotoImage(file="../View/Pictures/finish.png")
        Label(root2, image=finishPhoto, bd=0).grid(row=3, column=5)
        root2.mainloop()
        return

    r = StringVar()
    Label(frame, text='Question Number: ' + str(i + 1)+"  Of "+str(len(result)), bg='#064134', font=11, fg='yellow',pady=40).grid(row=4, column=1)
    question_label= Label(frame, text=result[i][1],fg='#F39C12',bg='#064134',font=10,padx=20)
    question_label.grid(row=5, column=1)
    ans1=Radiobutton(frame,text=result[i][2],variable=r,value=result[i][2],bg='#064134',font=10)
    ans1.grid(row=6,column=1)
    ans1.select()
    ans2=Radiobutton(frame,text=result[i][3],variable=r,value=result[i][3],bg='#064134',font=10)
    ans2.grid(row=7,column=1)
    ans2.select()
    ans3= Radiobutton(frame,text=result[i][4],variable=r,value=result[i][4],bg='#064134',font=10)
    ans3.grid(row=8,column=1)
    ans3.select()
    def clicked(value):
        global j
        Label(frame,text="correct answer is: "+result[i][5],bg='#064134',fg='yellow').grid(row=11,column=1)
        if value == result[i][5]:
            Label(frame,text='correct answer '+emoji.emojize(":grinning_face_with_big_eyes:"),bg='#064134',fg='yellow',font=10).grid(row=12,column=1)
            j=j+1

        else:
            Label(frame,text='wrong answer'+emoji.emojize(":thinking_face:"),bg='#064134',fg='red',font=10).grid(row=12,column=1)
        #ans1.configure(state=DISABLED)
        #ans2.configure(state=DISABLED)
        #ans3.configure(state=DISABLED)
        ans1.deselect()
        ans2.deselect()
        ans3.deselect()
    btn=Button(frame,text="answer",command=lambda: clicked(r.get()))
    btn.grid(row=9, column=1)



def select():
    mylabel.config(text=ListAct.get(ANCHOR))
    activity_id = (ListAct.get(ANCHOR)[0],)
    mycursor.execute(sql2, activity_id)
    result = mycursor.fetchall()
    root.destroy()
    root1 = Tk()
    root1.title("play activity")
    root1['background'] = '#69966d'
    root1.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
    root1.geometry("1000x1000")
    frame = Frame(root1,bg='#064134')
    frame.grid(row=2,column=0,ipady=100,ipadx=600)
    #addQuestion(frame,result,r)
    r = StringVar()
    Label(frame,text='Question Number: '+str(i+1)+"  Of "+str(len(result)),bg='#064134',font=11,fg='yellow',pady=40).grid(row=4,column=1)
    question_label = Label(frame, text=result[i][1], fg='#F39C12', bg='#064134', font=10,pady=10,padx=20)
    question_label.grid(row=5, column=1)
    ans1 = Radiobutton(frame, text=result[i][2], variable=r, value=result[i][2], bg='#064134', font=10)
    ans1.grid(row=6, column=1)
    ans1.select()
    ans2 = Radiobutton(frame, text=result[i][3], variable=r, value=result[i][3], bg='#064134', font=10)
    ans2.grid(row=7, column=1)
    ans2.select()
    ans3 = Radiobutton(frame, text=result[i][4], variable=r, value=result[i][4], bg='#064134', font=10)
    ans3.grid(row=8, column=1)
    ans3.select()

    def clicked(value):
        global j
        j=0
        Label(frame, text="correct answer is: " + result[i][5], bg='#064134',fg='yellow').grid(row=11, column=1)
        if value == result[i][5]:
            Label(frame, text='correct answer ' + emoji.emojize(":grinning_face_with_big_eyes:"), bg='#064134',fg='yellow', font=10).grid(row=12, column=1)
            j=j+1

        else:
            Label(frame, text='wrong answer' + emoji.emojize(":thinking_face:"), bg='#064134', fg='red', font=10).grid(
                row=12, column=1)
     #  ans1.configure(state=DISABLED)
      #  ans2.configure(state=DISABLED)
       # ans3.configure(state=DISABLED)
        ans1.deselect()
        ans2.deselect()
        ans3.deselect()
    btn = Button(frame, text="answer", bg='#F39C12',command=lambda: clicked(r.get()))
    btn.grid(row=9, column=1)
    next = PhotoImage(file="../View/Pictures/next.png")
    btn = Button(frame, image=next,bd=0, command=lambda: addQuestion(frame, result,root1))
    btn.grid(row=7, column=3)
    root1.mainloop()



mybtn=Button(root,text='Select and Start Activity',bg='#F39C12',pady=10,padx=20,command=select)
mybtn.grid(row=7,column=1,pady=20)
mylabel=Label(root,text='',padx=20,bg='#064134')
mylabel.grid(row=8,column=1)
root.mainloop()
