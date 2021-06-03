from tkinter import *
from PIL import Image, ImageTk
import webbrowser

root = Tk()

root.title("Searching For An Activity")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
photo = PhotoImage(file="../View/Pictures/logo.png")
Label(root, image=photo,bd=0).grid(row=2,column=2)
photo2= PhotoImage(file="../View/Pictures/pic.png")
Label(root, image=photo2,bd=0).grid(row=1,column=1)


root.mainloop()