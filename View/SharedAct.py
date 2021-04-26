from tkinter import *
from PIL import Image, ImageTk
import webbrowser

root = Tk()

root.title("Searching For An Activity")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
slb = Label(root, text="                                     ", bg='#064134')
slb.grid(row=0, column=1)
titleLb = Label(root, text='Your Group - Shared Activities', font=20, padx=40, pady=20, bg='#064134', fg='white')
titleLb.grid(row=0, column=30)

searchEnt = Entry(root, fg='gray')
searchEnt.grid(row=1, column=30, ipadx=40)
searchEnt.insert(0, 'search for group')
slb = Label(root, text="                                     ", bg='#064134')
slb.grid(row=2, column=1)
lb2 = Label(root, text='your groups that have new activities that you can participate in right now!', bg='#064134')
lb2.grid(row=2, column=30, ipadx=60, ipady=20)

Lb = Listbox(root, width=70, height=10)
Lb.grid(row=3, column=30)
root.mainloop()
