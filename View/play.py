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

def drag_start(event):
    widget=event.widget
    widget.startX=event.x
    widget.startY=event.y

def drag_motion(event):
    widget=event.widget
    x=widget.winfo_x()-widget.startX+event.x
    y=widget.winfo_y()-widget.startY+event.y
    widget.place(x=x,y=y)

def end_x(event):

    widget=event.widget
    x=widget.winfo_x()



root=Tk()
root['background']='#064134'
root.geometry("1000x1000")
vlist =["biology","chemistry","physics","math"]
Combofiled = ttk.Combobox(root, values=vlist)
Combofiled.set("select filed")
Combofiled.place(x=380,y=120)
List = Listbox(root, width=70, height=10,bg='#69966d',font=10,fg='yellow')
List.place(x=20,y=180)


sql="SELECT * FROM Classification WHERE filed=%s"
sql2="SELECT * FROM answers WHERE classificationid=%s"
def start():


    column1=List.get(ANCHOR)[3]
    column2=List.get(ANCHOR)[4]
    classify_id = (List.get(ANCHOR)[0],)
    mycursor.execute(sql2, classify_id)
    result = mycursor.fetchall()
    root.destroy()
    root1=Tk()
    root1['background'] = '#064134'
    root1.geometry("1000x1000")
    my_canvas = Canvas(root1, width=375, height=500, bg='white')
    my_canvas2 = Canvas(root1, width=375, height=500, bg='white')
    my_canvas.place(x=50, y=100)
    my_canvas2.place(x=425, y=100)
    l1 = Label(root1, text=column1, bg='yellow', fg='purple', font=20)
    l1.place(x=150, y=120)
    l2 = Label(root1, text=column2, bg='yellow', fg='purple', font=20)
    l2.place(x=500, y=120)
    Label(root1,text="Classify",font=50,fg='yellow',bg='#064134').place(x=400,y=50)
    # finish = Button(root1, text="finish",bg="orange",command=lambda:test(result))
    #  finish.place(x=400, y=580)
    for i in range(len(result)):
        l3 = Label(root1, text=result[i][2], width=5, height=2, bg="green", font=15)
        l3.place(x=900, y=300)
        l3.bind("<Button-1>", drag_start)
        l3.bind("<B1-Motion>", drag_motion)
        l3.bind("<ButtonRelease>", end_x)

    root1.mainloop()

def select():
    filed = Combofiled.get()
    mycursor.execute(sql, (filed,))
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        List.insert(END, myresult[i])



Button(root, text="search ", bg="orange", command=select,justify=CENTER,padx=20).place(x=400,y=150)
Button(root,text="select and start to classify",bg="orange",command=start,justify=CENTER,pady=10).place(x=380,y=450)
Label(root,text="search for a classification", font=20, pady=20, padx=20, bg='#064134', fg='white').place(x=320,y=40)

root.mainloop()