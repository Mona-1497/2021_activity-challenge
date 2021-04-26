from tkinter import *
import mysql.connector
import webbrowser
import os


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1",
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
email = Entry(root, fg='#DFE3EE')
email.insert(0, "username@mail.com")
email.grid(row=4, column=1, padx=50, pady=10)
password = Entry(root, fg='#DFE3EE')
password.insert(0, "password")
password.grid(row=5, column=1, padx=50, pady=20)


def checkLog(mail, password):
    for user in users:
        print(user[0])
        print(user[1])
        if user[0] == mail and password == user[1]:
            os.system('MainMenu.py')
            root.quit()
            return
    print("Incorrect information")
    return


login_button = Button(root, command=lambda: checkLog(email.get(), password.get()), text="Log in", bg='#69966d', font=10)
login_button.grid(row=6, column=1)


def open_attach():
    webbrowser.open("https://www.facebook.com/")


root.mainloop()


