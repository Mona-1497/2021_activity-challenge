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


mycursor.execute("Create TABLE IF NOT EXISTS users(Name VARCHAR(255) PRIMARY Key,Score INT, level INT) ")
mycursor.execute("Create TABLE IF NOT EXISTS AddActivity(id INT PRIMARY KEY AUTO_INCREMENT , level VARCHAR(255), filed VARCHAR(255),questionNum INT,description VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS questions(ActivityID INT  ,CONSTRAINT FOREIGN KEY (ActivityID) REFERENCES addactivity(id) ON UPDATE CASCADE  ON DELETE CASCADE,question VARCHAR(255)   ,answer1 VARCHAR(255) ,answer2 VARCHAR(255) ,answer3 VARCHAR(255) ,CorrectAnswer VARCHAR(255) )")
mycursor.execute("Create TABLE IF NOT EXISTS AddRiddle(id INT PRIMARY KEY AUTO_INCREMENT,filed VARCHAR(255),subject VARCHAR(255),riddlesNum INT )")
mycursor.execute("Create TABLE IF NOT EXISTS Riddle(RiddleID INT,CONSTRAINT FOREIGN KEY (RiddleID) REFERENCES addRiddle(id) ON UPDATE CASCADE  ON DELETE CASCADE,riddle VARCHAR(255),answer VARCHAR(255),explanation VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS Classification(id INT PRIMARY KEY AUTO_INCREMENT,filed VARCHAR(255) ,description VARCHAR(255),firstgroup VARCHAR(255),secondgroup VARCHAR(255),CardsNum INT)")
mycursor.execute("Create TABLE IF NOT EXISTS Answers(classificationid INT,CONSTRAINT FOREIGN KEY (classificationid) REFERENCES Classification(id) ON UPDATE CASCADE  ON DELETE CASCADE,classifiedTo VARCHAR(255),answer VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS matches(id INT PRIMARY KEY AUTO_INCREMENT,field VARCHAR(255),description VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS matching(MatchingID INT,CONSTRAINT FOREIGN KEY (MatchingID) REFERENCES matches(id) ON UPDATE CASCADE ON DELETE CASCADE ,value VARCHAR(255),ismachTo VARCHAR(255))")
mycursor.execute("Create TABLE IF NOT EXISTS addGroup (groupName  VARCHAR(255) PRIMARY KEY,userName VARCHAR(255),memberNum INT,currentMem INT)")
mycursor.execute("Create TABLE IF NOT EXISTS joinToGroup(groupName  VARCHAR(255) NOT NULL ,memberName VARCHAR(255) NOT NULL,CONSTRAINT FOREIGN KEY (groupName) REFERENCES addgroup(groupName) ON UPDATE CASCADE  ON DELETE CASCADE,CONSTRAINT FOREIGN KEY (memberName) REFERENCES users(Name) ON UPDATE CASCADE  ON DELETE CASCADE,PRIMARY KEY(groupName,memberName),joinDate DATETIME)")
mycursor.execute("Create TABLE IF NOT EXISTS sharedAct(groupName VARCHAR(255) NOT NULL,ActID INT NOT NULL,CONSTRAINT FOREIGN KEY (groupName) REFERENCES addgroup(groupName) ON UPDATE CASCADE  ON DELETE CASCADE ,CONSTRAINT FOREIGN KEY (ActID) REFERENCES addactivity(id) ON UPDATE CASCADE  ON DELETE CASCADE ,PRIMARY KEY(groupName,ActID))")




