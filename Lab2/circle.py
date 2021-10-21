from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys


def round(a):
    return int(a + 0.5)


xc,yc,r = 0,0,0

def readInput():
    global xc,yc,r
    print("Enter radius and coordinate of centre of circle as r x y:",end=" ")
    r,xc,yc = map(int,input().split())

def drawCircle(r,xc,yc):
    target = math.pi/4
    theta = 0
    factor = 500
    incr = 1/r
    while theta < target:
        x = r*math.cos(theta)
        y = r*math.sin(theta)
        setPixel(x + xc, y + yc)
        setPixel(-x + xc, -y + yc)
        setPixel(-x + xc, y + yc)
        setPixel(x + xc, -y + yc)
        setPixel(y + xc, x + yc)
        setPixel(-y + xc, -x + yc)
        setPixel(-y + xc, x + yc)
        setPixel(y + xc, -x + yc)
        theta+=incr

def init():
    glClearColor(1, 1, 1, 1.0) #Background color
    glColor3f(0,0,0) #Color for object on screen here it's point
    glPointSize(2.0) #Size of the point
    #Dividing the screen into x,y coordinates aka Projection Matrix
    gluOrtho2D(0,500,0,500) #left, right, bottom, top
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

def setPixel(xcoordinate,ycoordinate):
    """
    Method to plot point on the screen
    """
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()



def display():
    glClear(GL_COLOR_BUFFER_BIT) #Clearing the color buffer first before drawing anything
    drawCircle(r,xc,yc) #Draw the circle


def main():
    readInput() #Ask for input
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500) #Size of the window
    glutInitWindowPosition(710, 100) #Location of the window
    glutCreateWindow("Circle")
    init()
    glutDisplayFunc(lambda: display()) #Display function will be called to draw each frame
    glutMainLoop() #Main loop handles the callback to draw the frames

main()