from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import ttk

root = Tk()

root.title("Searching For An Activity")
root['background']='#064134'
root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
label=Label(root,text='search for an activity',font=20,pady=20,padx=20,bg='#064134',fg='white')
label.grid(row=1,column=1)
searchEntry=Entry(root,fg='gray')
searchEntry.grid(row=2 ,column=1,ipadx=40)
searchEntry.insert(0,'search by keyword')
s1=Label(root,text="   ",bg='#064134')
s1.grid(row=3,column=1)
vlist=["Easy","Medium","Hard"]
Combo = ttk.Combobox(root, values=vlist)
Combo.set("select level")

Combo.grid(row=9,column=1,ipadx=10)
s2=Label(root,text="   ",bg='#064134')
s2.grid(row=6,column=1)
l1=Label(root,text='Add Tags:                ',bg='#064134',fg='white',font=3)
l1.grid(row=4,column=1)
tagsentry=Entry(root)
tagsentry.grid(row=5,column=1,ipadx=40)
tag=tagsentry.get()
s3=Label(root,text="   ",bg='#064134')
s3.grid(row=8,column=1)
Lb = Listbox(root)
Lb.grid(row=7,column=1)
def clicked():
    tag=tagsentry.get()
    Lb.insert(1,tag)
def clearclicked():
    tag=Lb.get()
addbtn=Button(root,text="add",padx=10,command=clicked)
addbtn.grid(row=5,column=2)
clearbtn=Button(root,text="clear",padx=10,command=clearclicked)
clearbtn.grid(row=5,column=3)

searchbtn=Button(root,text='Search',bg='#69966d',font=30,width=10)
searchbtn.grid(row=10,column=1,pady=20)

root.mainloop()