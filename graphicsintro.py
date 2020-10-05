from graphics import *
from time import sleep
from random import randint
'''

The graphics library
         ___  __                                ______                 __    _          
       / __ \/ /_        ____ ___  __  __      / ____/________ _____  / /_  (_)_________
      / / / / __ \______/ __ `__ \/ / / /_____/ / __/ ___/ __ `/ __ \/ __ \/ / ___/ ___/
     / /_/ / / / /_____/ / / / / / /_/ /_____/ /_/ / /  / /_/ / /_/ / / / / / /__(__  ) 
     \____/_/ /_/     /_/ /_/ /_/\__, /      \____/_/   \__,_/ .___/_/ /_/_/\___/____/  
                                /____/                      /_/                         

Dylan Rodriquez 
CS177

'''


'''
===============================================
Upcomming:
    
    Labs and preps
    ========
    lp4

    l4
    ========
    
    PROJECT 1

    EXAM 1 - NEXT WEEK 

    ========

    Homework 6  Sunday



A note about the exam: 

    - exam environment
    - preparation
    - resources
    - all this will be on slides on brightspace

===============================================



The graphics library provides classes for creating graphics programs 
without having to rewrite code. 

These classes allow us to make graphics primitives (points and lines) as
well as polygons and other geometric shapes. Some shapes are predefined.


**
    A class contains data and methods that act on the data.
                                                            **


==========================
The graphics primitives
==========================

Point

Point(x, y)
'''
p1 = Point(2, 3)
print(type(p1))
p2 = Point(3, 4)

p1x = p1.getX()

print(p1x > p2.getX())

'''
getX()
getY()

circle(Point, radius)


        Point ----- rad


two point primitives


Line
point1, point2


Rect

p1---
|    |
-----p2

n point primitives:

polygon:

        p7
                    p6
  p8
                    p5
p1
                p4

                        p3
        p2


counter clockwise points




'''





w = 480
# win is an instance of the GraphWin class instantiated with three parameters.
                # name   #w   #h
win = GraphWin("window", w, w, autoflush = False)
estiwindow = GraphWin("Estimates", w,w, autoflush = False)
text = Text(Point(w/2, 30),"monte carlo estimate: pi")
text.draw(estiwindow)
piText = "Estimate of Pi: " 
pi  = Text(Point(w/2, 60), piText)
linex = Line(Point(0, w/4+ (480 - 314)),Point(640,w/4+(480 - 314)))
liney = Line(Point(10,2*w/8), Point(10,7.8*w/8))
linex.draw(estiwindow)
liney.draw(estiwindow)
pi.draw(estiwindow)

estimates = []
pointlist = []
pestimate = []
colored = 0
noncolored = 0
n = 10**4
for i in range(n):
    x = randint(1,w)
    y = randint(1,w)
    p = Point(x , y)
    if ((w/2 - x)**2 + (w/2-y)**2)**(1/2) < w/2:
        r = randint(1,255)
        g = randint(1,255)
        b = randint(1,255)
        p.setFill(color_rgb(r,g,b))
        colored +=1
        pointlist.append(p)
    else:
        p.setFill("black")
        pointlist.append(p)
        noncolored += 1
    montecarl = 4 * (colored)/ (colored +noncolored)
    estimates.append(4 * (colored)/ (colored +noncolored))
    p = Point(int((w - 50)*(i/n))+30, w/4+ (480 - 100*(estimates[i])))
    pestimate.append(p)
    pi.setText("{}{}".format(piText, montecarl))

def drawnpoints(n):
    for i in pointlist[:n]:
        print (i)
        i.draw(win)
    return pointlist[:n]

i = 0
while i < (len(pointlist)):
    drawnpoints(i)
    pestimate[i].draw(estiwindow) 
    update(100)

# win.getMouse is a method of GraphWin which gets the current position of the mouse
curPos = win.getMouse()
ps = estiwindow.getMouse()
print(curPos)
win.close()

