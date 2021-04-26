from tkinter import *
import mysql.connector
from datetime import date
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1",
    database="ActivityChallengeDB"
)

mycursor = mydb.cursor(buffered=True)


class Register:
    def __init__(self, name, lastName, birthDate, email, password, conPassword):
        self.name = name
        self.lastName = lastName
        self.birthDate = birthDate
        self.email = email
        self.password = password
        self.conPassword = conPassword

    mycursor.execute("""SELECT * FROM user;""")
    users = mycursor.fetchall()

    def register(self):
        if self.password == self.conPassword:
            for user in self.users:
                if user[0] == self.email:
                    print("User already exists")
                    return
            print(self.birthDate)
            print(date.today())
            mycursor.execute("""INSERT INTO User(mail, password, firstName, lastName, birthDate, joinDate) VALUES (
            %s, %s, %s, %s, %s, %s)""", (self.email, self.password, self.name, self.lastName, self.birthDate,
                                         date.today()))
            mydb.commit()
            os.system('SearchAndChooseAct.py')
        else:
            print(name)


root = Tk()
root.title("Sign Up")
root['background'] = '#064134'
# root.iconbitmap("C:/Users/Mona_/PycharmProjects/2021_activity-challenge")
root.geometry("1000x1000")
label1 = Label(root, text="Sign Up", fg='black', font=200, bg='#064134', pady=20)
label1.grid(row=1, column=0)
name = Entry(root, fg='#DFE3EE')
name.grid(row=2, column=0, pady=10)
name.insert(0, "first name")
space = Label(root, text="    ")
lName = Entry(root, fg='#DFE3EE')
lName.insert(0, "name")
lName.grid(row=2, column=3, pady=10)
birthdate = Entry(root, fg='#DFE3EE')
birthdate.grid(row=3, column=0, pady=10)
birthdate.insert(0, 'Birth date ')
email = Entry(root, fg='#DFE3EE')
email.insert(0, "username@mail.com")
email.grid(row=4, column=0, padx=50, pady=10)
password = Entry(root, fg='#DFE3EE')
password.insert(0, "password")
password.grid(row=5, column=0, padx=50, pady=10)

conPassword = Entry(root, fg='#DFE3EE')
conPassword.insert(0, "Confirm password")
conPassword.grid(row=6, column=0, padx=50, pady=10)
signUpButton = Button(root, text='Sign Up',
                      command=lambda: Register(name.get(), lName.get(), birthdate.get(), email.get(), password.get(),
                                               conPassword.get()).register(), bg='#69966d', font=30, width=10)

signUpButton.grid(row=7, column=0, pady=20)
root.mainloop()
