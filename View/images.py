from tkinter import *
from tkinter import ttk
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

root=Tk()
root['background'] = '#064134'
root.geometry("1000x1000")
e=Entry(root)
e.place(x=500,y=300)

def inserBlob(filepath):

    file = open(filepath, 'rb')
    if file is not None:
        content = file.read()
        sql="INSERT INTO img(name,photo)  VALUES (%s,%s)"
        mycursor.execute(sql,(content,))
        mydb.commit()
def retrive(name):
    sql2="SELECT * FROM img WHERE name=%s "
    mycursor.execute(sql2,(name, ))
    res=mycursor.fetchone()
    store=f"../View/Pictures/{name}.jpg",name
Button(root,text="insert",command=lambda :inserBlob(e.get())).place(x=500,y=400)

root.mainloop()