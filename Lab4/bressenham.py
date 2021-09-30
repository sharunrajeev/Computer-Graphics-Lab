import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def sign(num):
    if (num>0):
        return 1
    elif(num==0):
        return 0
    else:
        return -1

def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def line():
    x1 = int(input('Enter x1: '))
    y1 = int(input('Enter y1: '))
    x2 = int(input('Enter x2: '))
    y2 = int(input('Enter y2: '))
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    s1 = sign(x2-x1)
    s2 = sign(y2-y1)
    if (dy>dx):
        temp = dx 
        dx = dy
        dy = temp
        interchange = 100
    else:
        interchange = 0

    e = (2*dy)-dx
    glClear(GL_COLOR_BUFFER_BIT)
    # points
    glColor3f(1,0.5,0.6)
    glPointSize(7.0)
    glBegin(GL_POINTS)
    for i in range(1,dx):
        glVertex2f(x/100,y/100)
        while(e>0):
            if interchange==1:
                x = x + s1
            else:
                y=y+s2
            e = e-(2*dx)
        if interchange==1:
            y=y+s2
        else:
            x=x+s1
        e = e+(2*dy)
    glEnd()
    glFlush()




glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Bresenham")
glutInitWindowSize(200, 200)
glutInitWindowPosition(100, 100)
glutDisplayFunc(line)
clearScreen()
glutMainLoop()
