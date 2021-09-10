import  turtle

def draw_rec_1():
    t = turtle.Turtle()

    t.penup()
    t.goto(-90, 150)
    t.pendown()

    t.color("orange")
    t.begin_fill()
    for i in range(2):
        t.fd(180)
        t.rt(90)
        t.fd(300)
        t.rt(90)

    t.penup()
    t.goto(-90, 0)
    t.pendown()
    t.fd(180)

    t.penup()
    t.goto(0, 150)
    t.pendown()
    t.rt(90)
    t.fd(300)

    t.end_fill()



def draw_rec_2():
    t = turtle.Turtle()

    t.penup()
    t.goto(-60, 100)
    t.pendown()


    for j in range(2):
        t.fd(30)
        t.rt(90)
        t.fd(50)
        t.rt(90)

    t.penup()
    t.goto(30, 100)
    t.pendown()
    for j in range(2):
        t.fd(30)
        t.rt(90)
        t.fd(50)
        t.rt(90)

    t.penup()
    t.goto(-60, -50)
    t.pendown()
    for j in range(2):
        t.fd(30)
        t.rt(90)
        t.fd(50)
        t.rt(90)

    t.penup()
    t.goto(30, -50)
    t.pendown()
    for j in range(2):
        t.fd(30)
        t.rt(90)
        t.fd(50)
        t.rt(90)



def draw_rec_3():
    t = turtle.Turtle()

    t.penup()
    t.goto(90, 0)
    t.pendown()


    for i in range(2):
        t.fillcolor("red")
        t.begin_fill()
        t.fd(120)
        t.rt(90)
        t.fd(150)
        t.rt(90)
        t.end_fill()

    t.penup()
    t.goto(120, -75)
    t.pendown()

    for i in range(2):
        t.fd(60)
        t.rt(90)
        t.fd(75)
        t.rt(90)

    t.penup()
    t.goto(150, -75)
    t.pendown()
    t.rt(90)
    t.fd(75)
    turtle.done




hcn_1 = draw_rec_1()

hcn_2 = draw_rec_2()

hcn_3 = draw_rec_3()

