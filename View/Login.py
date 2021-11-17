from tkinter import *
import mysql.connector
import webbrowser
import os
current_user = os.getlogin()
print(current_user)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mona100%",
    database="ActivityChallengeDB"
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("""SELECT * FROM user;""")
users = mycursor.fetchall()


root = Tk()
root.title("Login")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")

welcome = Label(root, text="Log In", font=200, fg='black', bg='#064134')
welcome.grid(row=1, column=1, padx=170, pady=20)

label1 = Label(root, text="Log in with an existing email", bg='white', fg='black')
email = Entry(root,text="username@mail.com")
email.grid(row=4, column=1, padx=50, pady=10)
password = StringVar()
password = Entry(root,textvariable=password, show='*')
password.insert(0, "password")
password.grid(row=5, column=1, padx=50, pady=20)


def checkLog(mail, password):
    for user in users:
        print(user[0])
        print(user[1])
        if user[0] == mail and password == user[1]:
            root.destroy()
            os.system('MainMenu.py')
            return
    message=Label(root,text="Incorrect information",bg='#064134',pady=10)
    message.grid(row=7,column=1)
    return


login_button = Button(root, command=lambda: checkLog(email.get(), password.get()), text="Log in", bg='#69966d', font=10)
login_button.grid(row=6, column=1)




root.mainloop()


