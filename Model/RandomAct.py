from tkinter import *
from PIL import Image,ImageTk
import webbrowser

root = Tk()

root.title("Search Random Activity")
root['background']='#064134'
root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
ltitle=Label(root,text='                     Participate in a random activity',font=20,pady=20,padx=20,bg='#064134',fg='white')
ltitle.grid(row=0,column=1)
sellb=Label(root,text='     select an activity: ',font=10,bg='#064134',fg='white',pady=20)
sellb.grid(row=1,column=0)

Lb = Listbox(root,width=70,height=20)
Lb.grid(row=2,column=1)
root.mainloop()