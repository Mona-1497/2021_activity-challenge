import os
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
root.geometry("1000x1000")
root['background']='#064134'
title=Label(root,text="Find Matches",font=40,bg='#064134',fg='yellow')
title.pack(pady=10)
frame=Frame(root,bg="#064134")
frame.pack(pady=10)
sql="SELECT * FROM matching"
mycursor.execute(sql)
result=mycursor.fetchall()
values=[]
for i in range (0,len(result)):
    values.append(result[i][1])
count=0
ans_list=[]
ans_dict={}
lb=Label(root,text='',bg="#064134",font=20,fg='yellow')

def clicked(btn,number):
    global count,ans_list,ans_dict
    if btn["text"]==' ' and count<2:
        btn["text"]=values[number]
        ans_list.append(number)
        ans_dict[btn]=values[number]
        count=count+1
    if len(ans_list)==2:
        if result[ans_list[0]][2] == result[ans_list[1]][2]:
            lb.config(text="match!")
            for key in ans_dict:
                key["state"]="disabled"
            count = 0
            ans_list = []
            ans_dict = {}
        else:
            lb.config(text="try again!!")
            count = 0
            ans_list = []
            for key in ans_dict:
                key["text"]=" "
            ans_dict={}
    else:
        btn["text"] = values[number]



#input number of buttons
#row=0
#column=0
#for i in range (0,10):

 #   if i%3 == 0:
  #      row=row+1
   #    btn= Button(frame, text=' ', width=6, height=3, bg='green',command= lambda:clicked(btn,i))
    #    btn.grid(row=row,column=column)
     #   column=column+1
    #else:
     #  btn= Button(frame, text=' ', width=6, height=3, bg='green',command= lambda:clicked(btn,i))
      # btn.grid(row=row,column=column)
       #column=column+1
btn0= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn0,0),bg='orange')
btn1= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn1,1),bg='orange')
btn2= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn2,2),bg='orange')
btn3= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn3,3),bg='orange')
btn4= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn4,4),bg='orange')
btn5= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn5,5),bg='orange')
btn6= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn6,6),bg='orange')
btn7= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn7,7),bg='orange')
btn8= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn8,8),bg='orange')
btn9= Button(frame, text=' ', width=12, height=7,command= lambda:clicked(btn9,9),bg='orange')

btn0.grid(row=0,column=0)
btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=1,column=0)
btn4.grid(row=1,column=1)
btn5.grid(row=1,column=2)
btn6.grid(row=2,column=0)
btn7.grid(row=2,column=1)
btn8.grid(row=2,column=2)
btn9.grid(row=3,column=0)
lb.pack(pady=10)

def back():
    root.destroy()
    os.system('options.py')
photo = PhotoImage(file="../View/Pictures/back.png")
mybtn=Button(root,image=photo,bg='#F39C12',pady=10,padx=20,command=back)
mybtn.place(x=700,y=200)
root.mainloop()