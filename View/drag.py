import turtle
import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mona100%",
    database="ActivityChallengeDB",
)

def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


mycursor = mydb.cursor(buffered=True)
sql="Select * from questions where ActivityID=%s"
mycursor.execute(sql,(1,))
result = mycursor.fetchall()
wn=turtle.Screen()
wn.title("lets play")
wn.bgcolor("black")
wn.setup(width=800,height=600)
#wn.bgpic("C://Users//Mona_//PycharmProjects//2021_activity-challenge//Pictures//stars.jpg")

#BAll

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(10)
ball.penup()
ball.goto(0,200)
ball.dx=0
ball.dy=-2
style = ('Courier', 20, 'italic')
ball.fillcolor("gray")


pen=ball.getpen()
pen.write(result[0][1], font=style, align='center',move=True)


def quit():
    global flag
    flag=False
wn.listen()
wn.onkeypress(quit,"q")
flag=True
i=0
while flag:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if (ball.ycor()+ball.dy)==-600 and i<len(result)-1:
        i = i + 1
        pen.clear()
        print(result[i][1])
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        ball.shapesize(10)
        ball.penup()
        ball.goto(0, 300)
        ball.dx = 0
        ball.dy = -2
        ball.fillcolor("gray")
        pen1 = ball.getpen()
        pen1.write(result[i][1], font=style, align='center', move=True)
        name = turtle.textinput("question no. "+str(i), "answer")

