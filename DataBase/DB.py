import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS ActivityChallengeDB")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1",
    database="ActivityChallengeDB"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS user (mail VARCHAR(255) PRIMARY KEY, password VARCHAR(255), firstName "
                 "VARCHAR(255), lastName VARCHAR(255), birthDate DATETIME, phone VARCHAR(255), joinDate DATETIME)")

mycursor.execute("CREATE TABLE IF NOT EXISTS friendlist (mail1 VARCHAR(255), mail2 VARCHAR(255), dateAdding DATETIME, "
                 "PRIMARY KEY (mail1, mail2))")

mycursor.execute("CREATE TABLE IF NOT EXISTS friendrequest (tomail VARCHAR(255), frommail VARCHAR(255), daterequest "
                 "DATETIME, confirm BOOLEAN, PRIMARY KEY(tomail, frommail))")

mycursor.execute("CREATE TABLE IF NOT EXISTS joinrequest (teamid INT PRIMARY KEY, managermail VARCHAR(255), "
                 "usermail VARCHAR(255), confirm BOOLEAN, daterequest DATETIME)")

mycursor.execute("CREATE TABLE IF NOT EXISTS manage (teamid INT PRIMARY KEY, managermail VARCHAR(255), startdate "
                 "DATETIME)")

mycursor.execute("CREATE TABLE IF NOT EXISTS manager (id INT PRIMARY KEY AUTO_INCREMENT, description VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS post (id INT PRIMARY KEY AUTO_INCREMENT, photo VARCHAR(255), "
                 "text VARCHAR(255), video VARCHAR(255), dateposted DATETIME)")

mycursor.execute("CREATE TABLE IF NOT EXISTS team (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))")
