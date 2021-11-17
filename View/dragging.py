import os
from random import random
from tkinter import *
from tkinter import ttk
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
sql1= "SELECT * FROM riddle "
mycursor.execute(sql1,)
result=mycursor.fetchall()
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
    k=0
    while k<5:
        if act2[k].get(widget) !=None:
           k = k+1
        k=k+1


    return

root1=Tk()
root1['background'] = '#064134'
root1.geometry("1000x1000")
act1=[]
act2=[]
#set labels randomly
for i in range(0, 5):
    flag = False
    Q = Label(root1, text=result[i][1], width=15, height=10,wraplength=80, font=("Comic Sans MS", 10))
    Q.place(x=random.randint(0,800), y=random.randint(0,600))
    Q.bind("<Button-1>", drag_start)
    root1.update()
    Q.bind("<B1-Motion>", drag_motion)
    A = Label(root1, text=result[i][3], width=15, height=10, wraplength=80, font=("Comic Sans MS", 10))
    A.place(x=random.randint(0, 800), y=random.randint(0, 600))
    A.bind("<Button-1>", drag_start)
    root1.update()
    A.bind("<B1-Motion>", drag_motion)
    act1.append({Q:(Q.winfo_x(),Q.winfo_y())})
    act2.append({A:(A.winfo_x(),A.winfo_y())})



root1.mainloop()
