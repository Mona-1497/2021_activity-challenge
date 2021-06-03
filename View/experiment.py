from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("1000x1000")

frame=Frame(root,width=200,height=300)
frame.pack(pady=20)
title=Label(frame,text="experiment name",pady=20)
title.grid(row=0 ,column=0)
name=Entry(frame,bg='#4ED8BE')
name.grid(row=1,column=0)
desc=Label(frame,text="experiment description:")
desc.grid(row=2,column=0)
textdesc=Text(frame,width=60,height=10)
textdesc.grid(row=3,column=0)
step=Label(frame,text="experiment steps:")
step.grid(row=4,column=0)
steptext=Text(frame,width=60,height=10)
steptext.grid(row=5,column=0)

root.mainloop()