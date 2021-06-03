import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mona100%"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS ActivityChallengeDB")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mona100%",
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

mycursor.execute("CREATE TABLE IF NOT EXISTS team (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(50))")


mycursor.execute("Create TABLE IF NOT EXISTS AddActivity(id INT PRIMARY KEY AUTO_INCREMENT , level VARCHAR(255), filed VARCHAR(255),language VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS questions(ActivityID INT  ,CONSTRAINT FOREIGN KEY (ActivityID) REFERENCES addactivity(id) ON UPDATE CASCADE  ON DELETE CASCADE,question VARCHAR(255),answer1 VARCHAR(255),answer2 VARCHAR(255),answer3 VARCHAR(255),CorrectAnswer VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS AddRiddle(id INT PRIMARY KEY AUTO_INCREMENT,filed VARCHAR(255),subject VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS Riddle(RiddleID INT,CONSTRAINT FOREIGN KEY (RiddleID) REFERENCES addRiddle(id) ON UPDATE CASCADE  ON DELETE CASCADE,riddle VARCHAR(255),answer VARCHAR(255),explanation VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS Classification(id INT PRIMARY KEY AUTO_INCREMENT,filed VARCHAR(255) ,description VARCHAR(255),firstgroup VARCHAR(255),secondgroup VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS Answers(classificationid INT,CONSTRAINT FOREIGN KEY (classificationid) REFERENCES Classification(id) ON UPDATE CASCADE  ON DELETE CASCADE,classifiedTo VARCHAR(255),answer VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS matches(id INT PRIMARY KEY AUTO_INCREMENT,field VARCHAR(255),description VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS matching(MatchingID INT,CONSTRAINT FOREIGN KEY (MatchingID) REFERENCES matches(id) ON UPDATE CASCADE ON DELETE CASCADE ,value VARCHAR(255),ismachTo VARCHAR(255))")
