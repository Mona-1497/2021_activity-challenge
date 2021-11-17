
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import os
import mysql.connector
from datetime import date

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
    def __init__(self,groupName,userName,memberNum,currentMem):
        self.groupName=groupName
        self.userName=userName
        self.memberNum=memberNum
        self.currentMem=currentMem

    def addGroup(self):
        mycursor.execute(sql, )
        res = mycursor.fetchall()
        for k in range (len(res)):
            if(res[k][0]==self.groupName):

                return False

        mycursor.execute("""INSERT INTO addGroup (groupName,userName,memberNum,currentMem)
                          VALUES (%s, %s,%s,%s)""", (self.groupName,self.userName,self.memberNum,self.currentMem))
        mydb.commit()
        return True

root = Tk()
root.title("Groups")
root['background'] = '#064134'
root.geometry("1920x1080")
Font= ("Comic Sans MS", 30, "bold")
title = Label(root, text='Groups', bg='#064134', font=Font, fg='orange', pady=10)
title.place(x=480,y=30)

def add(groupname,memberNum,avlb):
    group = Group(groupname, current_user,memberNum,0)
    if group.addGroup()== False:
        avlb.config(text='duplicate group name')
    else:
      avlb.config(text='group added')



def createGroup():
    root.destroy()
    root2=Tk()
    root2.title("Groups")
    root2['background'] = '#064134'
    root2.geometry("1920x1080")
    Font = ("Comic Sans MS", 30, "bold")
    title = Label(root2, text='Create Group', bg='#064134', font=Font, fg='orange', pady=10)
    title.place(x=450, y=30)
    gn=Entry(root2,width=50)
    gn.insert(0,'group name')
    gn.place(x=450,y=150)
    w = Spinbox(root2, from_=1, to=10)
    w.place(x=450,y=200)
    avlb = Label(root2, text='', bg='#064134', fg='orange', font=12)
    avlb.place(x=500, y=350)
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/groupbtn.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    joinimg = ImageTk.PhotoImage(resized_image)
    Button(root2,text='create group',bg='#064134',font=("bold",12),image=joinimg,compound=LEFT,bd=0,fg='white',command=lambda: add(gn.get(),w.get(),avlb)).place(x=450,y=250)

    def callback4():
        root2.destroy()
        os.system('MainMenu.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(resized_image)
    homebtn = Button(root2, image=photo4, command=callback4, borderwidth=0, bg='#064134')
    homebtn.place(x=20, y=20)


    def back():
        root2.destroy()
        os.system('groups.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    mybtn = Button(root2, image=photo, pady=10, padx=20, command=back,bd=0,bg='#064134')
    mybtn.place(x=20, y=580)
    root2.mainloop()


sql = "SELECT groupName from addGroup"
sqlselect = "SELECT memberNum from addGroup where groupName=%s"
sqlselect2 = "SELECT currentMem from addGroup where groupName=%s"
sqljoined="SELECT groupName from joinToGroup WHERE memberName=%s"

def select(name,lb):
  try:
    mycursor.execute(sqlselect,(name,))
    memNum = mycursor.fetchall()
    mycursor.execute(sqlselect2, (name,))
    curNum = mycursor.fetchall()
    if curNum[0][0]<memNum[0][0]:
      x=curNum[0][0]
      x=x+1
      mycursor.execute("""INSERT INTO joinTogroup (groupName,memberName,joinDate)
                              VALUES (%s, %s,%s)""", (name,current_user,date.today()))
      mycursor.execute("""UPDATE addgroup
                       SET currentMem=%s
                          WHERE groupName=%s""",(x,name))
      mydb.commit()
      lb.config(text='joined to '+name+' group')


    else:
      lb.config(text='Sorry group is completed')
  except:
      lb.config(text="please choose group")

def joinGroup():
    root.destroy()
    root3=Tk()
    root3.title("Groups")
    root3['background'] = '#064134'
    root3.geometry("1920x1080")
    Font = ("Comic Sans MS", 30, "bold")
    title = Label(root3, text='Join Group', bg='#064134', font=Font, fg='orange', pady=10)
    title.place(x=450, y=30)
    mycursor.execute(sql,)
    res=mycursor.fetchall()
    mycursor.execute(sqljoined,(current_user,) )
    res2 = mycursor.fetchall()
    #disjoin group List with group that already joined
    myres=list(set(res) ^ set(res2))
    Listgropus = Listbox(root3, width=40, height=10, bg='#69966d', font=10, fg='#001a00')
    Listgropus.place(x=400,y=150)
    for i in range(len(myres)):
        Listgropus.insert(END, myres[i][0])
    lb2 = Label(root3, bg='#064134', fg='orange',font=12)
    lb2.place(x=500,y=420)
    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/groupbtn.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    joinimg = ImageTk.PhotoImage(resized_image)
    Button(root3,text=" join group",image=joinimg,compound=LEFT,bd=0,fg='white',font=("bold",12), bg='#064134',command=lambda :select(Listgropus.get(ANCHOR),lb2)).place(x=500,y=400)

    def back():
        root3.destroy()
        os.system('groups.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
    resized_image = img.resize((80, 60), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    mybtn = Button(root3, image=photo, pady=10, padx=20, command=back,bg='#064134',bd=0)
    mybtn.place(x=20, y=580)

    def callback4():
        root3.destroy()
        os.system('MainMenu.py')

    img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/home.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(resized_image)
    homebtn = Button(root3, image=photo4, command=callback4, borderwidth=0, bg='#064134')
    homebtn.place(x=20, y=20)
    root3.mainloop()

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/addgroup.png"))
resized_image = img.resize((200, 200), Image.ANTIALIAS)
create = ImageTk.PhotoImage(resized_image)
Button(root,image=create,fg='white',font=("Comic Sans MS", 30, "bold"),command=createGroup,bg='#064134',bd=0).place(x=300,y=200)
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/join2.png"))
resized_image = img.resize((200, 200), Image.ANTIALIAS)
join = ImageTk.PhotoImage(resized_image)
Button(root,image=join,fg='white',font=("Comic Sans MS", 30, "bold"),command=joinGroup,bg='#064134',bd=0).place(x=650,y=200)
def back():
    root.destroy()
    os.system('MainMenu.py')
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,pady=10,padx=20,command=back,bg='#064134',bd=0)
mybtn.place(x=20,y=580)
root.mainloop()