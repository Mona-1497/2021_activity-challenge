from tkinter import *
import os
from PIL import ImageTk, Image, ImageDraw
import mysql.connector
from tkinter import ttk
import time


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
root.title("Start Activity Challenge")
root['background'] = '#064134'
root.geometry("1920x1080")
Font= ("Times New Roman", 40, "bold")
title = Label(root, text='Activity Challenge', bg='#064134', font=Font, fg='orange', pady=10)
title.place(x=400,y=50)
current_user = os.getlogin()

sql="SELECT Name FROM users"
mycursor.execute(sql,)
myres=mycursor.fetchall()
Font2= ("Times New Roman", 15, "bold")
proglb=Label(root,text='',bg='#064134', font=Font2, fg='#00e6b8')
proglb.place(x=550,y=570)
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='#00e6b8', background='#00e6b8',troughcolor='gray')
progress=ttk.Progressbar(root,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=1250,mode='determinate')
progress.place(x=15,y=600)
#def step():
    #while progress['value']<100:
      #progress['value']+=1
      #proglb.config(text=(int(progress['value']),"%"))
     # root.update_idletasks()
    #  time.sleep(0.05)

   # root.destroy()
  #  os.system('MainMenu.py')






global flag
flag=False
def start():
    global flag
    flag=False
    for i in range (len(myres)):
        if myres[i][0]==current_user:
            flag=True
    if flag==False:
      mycursor.execute("""INSERT INTO users (Name,Score,level)
                    VALUES (%s, %s, %s)""",(current_user,0,1))
      mydb.commit()
    while progress['value'] < 100:
        progress['value'] += 10
        proglb.config(text=(int(progress['value']), "%"))
        root.update_idletasks()
        time.sleep(0.05)
    root.destroy()
    os.system('MainMenu.py')

img = (Image.open("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures/play3.png"))
resized_image = img.resize((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
startBtn = Button(root, image=photo, padx=100, bd=0, command=start,bg='#064134')
startBtn.place(x=450,y=220)


root.mainloop()