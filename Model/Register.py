from tkinter import *
from PIL import Image,ImageTk
import webbrowser
root = Tk()
root.title("Sign Up")
root['background']='#064134'
root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
label1=Label(root,text="Sign Up",fg='black',font=200,bg='#064134',pady=20)
label1.grid(row=1,column=0)
name=Entry(root,fg='#DFE3EE')
name.grid(row=2,column=0,pady=10)
name.insert(0,"first name")
space=Label(root, text="    ")
lname = Entry(root,fg='#DFE3EE')
lname.insert(0,"name")
lname.grid(row=2,column=3,pady=10)
birthdate=Entry(root,fg='#DFE3EE')
birthdate.grid(row=3,column=0,pady=10)
birthdate.insert(0,'Birth date ')
email=Entry(root,fg='#DFE3EE')
email.insert(0,"username@mail.com")
email.grid(row=4,column=0,padx=50,pady=10)

password=Entry(root,fg='#DFE3EE')
password.insert(0,"password")
password.grid(row=5,column=0,padx=50,pady=10)

conpassword=Entry(root,fg='#DFE3EE')
conpassword.insert(0,"Confirm password")
conpassword.grid(row=6,column=0,padx=50,pady=10)

signupbutton=Button(root,text='Sign UP',bg='#69966d',font=30,width=10)
signupbutton.grid(row=7,column=0,pady=20)
root.mainloop()
