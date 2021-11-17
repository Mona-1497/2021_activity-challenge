from tkinter import *
import mysql.connector
import os
from PIL import ImageTk,Image
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

root = Tk()
root.title("Profile")
root['background'] = '#064134'
root.geometry("1920x1080")
current_user = os.getlogin()
Label(root,text=current_user+"'s Profile",bg='#064134',fg='orange',font=("Comic Sans MS", 30, "bold")).place(x=400,y=40)
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/level.png"))
resized_image = img.resize((100, 100), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(resized_image)
Label(root,bg='#064134',image=photo2).place(x=400,y=150)
#Label(root,bg='#064134',text='level',fg='#ffff80',font=("Comic Sans MS", 15)).place(x=430,y=230)

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/score.png"))
resized_image = img.resize((100, 100), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(resized_image)
Label(root,bg='#064134',image=photo3).place(x=600,y=140)

sql="SELECT Score ,level From users WHERE Name=%s"
mycursor.execute(sql,(current_user,) )
res = mycursor.fetchall()
#res[0][0]:score
#res[0][1]:level
lb=Label(root,text=" "+str(res[0][1]),bg='#064134',fg='#ccff99',font=("Comic Sans MS", 15))
lb.place(x=420,y=240)

score=res[0][0]
Label(root,text=str(res[0][0])+" Points",bg='#064134',fg='#ccff99',font=("Comic Sans MS", 15)).place(x=600,y=240)
#level Update(five levels)
#0-20 1, 20-50 2 50-90 3 90-140 4 140- 5
if score>=0 and score<=20:
    mycursor.execute("""UPDATE users
                                  SET level=%s
                                     WHERE Name=%s""", (1, current_user))
    mydb.commit()
    lb.config(text=" Level 1")
if score>20 and score<=50:
    mycursor.execute("""UPDATE users
                               SET level=%s
                                  WHERE Name=%s""", (2, current_user))
    mydb.commit()
    lb.config(text=" Level 2")

if score>50 and score<=90:
    mycursor.execute("""UPDATE users
                                  SET level=%s
                                     WHERE Name=%s""", (3, current_user))
    mydb.commit()
    lb.config(text="Level 3")

if score > 90 and score <= 140:
    mycursor.execute("""UPDATE users
                                  SET level=%s
                                     WHERE Name=%s""", (4, current_user))
    mydb.commit()
    lb.config(text="Level 4")

if score > 140:
    mycursor.execute("""UPDATE users
                                  SET level=%s
                                     WHERE Name=%s""", (5, current_user))

    mydb.commit()
    lb.config(text="Level 5")


#group list
sql2="SElECT groupName from joinToGroup where memberName=%s"
sql3="DELETE From joinToGroup Where groupName=%s AND memberName=%s"
sqlselect2="SELECT currentMem from addGroup where groupName=%s"
mycursor.execute(sql2,(current_user,))
result=mycursor.fetchall()
Label(root,text='Groups You Joined:',bg='#064134',fg='#ccff99',font=("Comic Sans MS", 15)).place(x=400,y=320)
Lb = Listbox(root, width=30, height=5,bg='#69966d',font=10,fg='#001a00')
Lb.place(x=400 ,y=360)

for i in range(len(result)):
    Lb.insert(END, result[i])
indexlb=Label(root, text='', bg='#064134', fg='red', font=("Comic Sans MS", 15))
indexlb.place(x=450, y=560)
def leave():
    try:
     groupName = (Lb.get(ANCHOR)[0],)
     mycursor.execute(sql3,(groupName[0],current_user))
     mydb.commit()
     #Lb.delete(0,END)
     indexlb.config(text='left group')
     mycursor.execute(sqlselect2, (groupName[0],))
     curNum = mycursor.fetchall()
     x = curNum[0][0]
     x = x - 1
     mycursor.execute("""UPDATE addgroup
                           SET currentMem=%s
                              WHERE groupName=%s""", (x, groupName[0]))
     mydb.commit()
    except:
       indexlb.config(text="please choose group")



img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/leave.png"))
resized_image = img.resize((50,50), Image.ANTIALIAS)
lev = ImageTk.PhotoImage(resized_image)

Button(root,text='leave group',image=lev,compound=LEFT,bg='#064134',fg='white',bd=0,font=("bold", 12),command=leave).place(x=450,y=500)
def back():
    root.destroy()
    os.system('MainMenu.py')
img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/back.png"))
resized_image = img.resize((80, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
mybtn=Button(root,image=photo,bd=0,bg='#064134',command=back)
mybtn.place(x=20,y=580)
root.mainloop()