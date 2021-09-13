
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import os
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

class Group:
    def __init__(self,groupName,userName,memberNum):
        self.groupName=groupName
        self.userName=userName
        self.memberNum=memberNum

    def addGroup(self):
        mycursor.execute("""INSERT INTO addGroup (groupName,userName,memberNum)
                          VALUES (%s, %s,%s)""", (self.groupName,self.userName,self.memberNum))
        mydb.commit()


root = Tk()
root.title("Groups")
root['background'] = '#064134'
root.geometry("1000x1000")
Font= ("Comic Sans MS", 30, "bold")
title = Label(root, text='Groups', bg='#064134', font=Font, fg='orange', pady=10)
title.place(x=450,y=30)

def add(groupname,memberNum,root2):
    group = Group(groupname, current_user,memberNum)
    group.addGroup()
    Label(root2,text='group added').place(x=500,y=250)



def createGroup():
    root.destroy()
    root2=Tk()
    root2.title("Groups")
    root2['background'] = '#064134'
    root2.geometry("1000x1000")
    Font = ("Comic Sans MS", 30, "bold")
    title = Label(root2, text='Create Group', bg='#064134', font=Font, fg='orange', pady=10)
    title.place(x=450, y=30)
    gn=Entry(root2,width=50)
    gn.insert(0,'group name')
    gn.place(x=450,y=150)
    w = Spinbox(root2, from_=0, to=10)
    w.place(x=450,y=200)
    Button(root2,text='create group',width=15,bg='#ff3300',fg='white',font=("Comic Sans MS", 25, "bold"),command=lambda: add(gn.get(),w.get(),root2)).place(x=450,y=300)


    def back():
        root2.destroy()
        os.system('groups.py')

    img = (Image.open("../View/Pictures/bb.png"))
    resized_image = img.resize((80, 50), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    mybtn = Button(root2, image=photo, pady=10, padx=20, command=back)
    mybtn.place(x=20, y=600)
    root2.mainloop()
sql="SELECT groupName from addGroup"

def select(name):
    mycursor.execute("""INSERT INTO joinTogroup (groupName,memberName)
                              VALUES (%s, %s)""", (name,current_user))
    mydb.commit()
def joinGroup():
    root.destroy()
    root3=Tk()
    root3.title("Groups")
    root3['background'] = '#064134'
    root3.geometry("1000x1000")
    Font = ("Comic Sans MS", 30, "bold")
    title = Label(root3, text='Join Group', bg='#064134', font=Font, fg='orange', pady=10)
    title.place(x=450, y=30)
    mycursor.execute(sql,)
    res=mycursor.fetchall()
    Listgropus = Listbox(root3, width=70, height=10, bg='#69966d', font=10, fg='yellow')
    Listgropus.place(x=200,y=150)
    for i in range(len(res)):
        Listgropus.insert(END, res[i][0])
    Button(root3,text="join group",width=15,bg='#ff3300',fg='white',font=("Comic Sans MS", 25, "bold"),command=lambda :select(Listgropus.get(ANCHOR))).place(x=450,y=500)



    def back():
        root3.destroy()
        os.system('groups.py')

    img = (Image.open("../View/Pictures/bb.png"))
    resized_image = img.resize((80, 50), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    mybtn = Button(root3, image=photo, pady=10, padx=20, command=back)
    mybtn.place(x=20, y=600)
    root3.mainloop()





Button(root,text='Create Group',fg='white',font=("Comic Sans MS", 30, "bold"),command=createGroup,width=15,bg='#ff3300').place(x=350,y=200)
Button(root,text='Join Group',fg='white',font=("Comic Sans MS", 30, "bold"),command=joinGroup,width=15,bg='#ff3300').place(x=350,y=400)
def back():
    root.destroy()
    os.system('MainMenu.py')
img = (Image.open("../View/Pictures/bb.png"))
resized_image = img.resize((80, 50), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,pady=10,padx=20,command=back)
mybtn.place(x=20,y=600)
root.mainloop()