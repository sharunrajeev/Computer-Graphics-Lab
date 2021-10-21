from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def DDA_Line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    if abs(dx) > abs(dy):
        n = round(math.log(dx)/math.log(2))

    else:
        n = round(math.log(dy)/math.log(2))

    deltax = abs(dx)/(2**n)
    deltay = abs(dy)/(2**n)

    for i in range(n):
        x0 += deltax
        y0 += deltay
        setPixel(round(x0), round(y0))


def setPixel(x, y):
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-100, 100, -100, 100)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    DDA_Line(x0, y0, x1, y1)
    glFlush()

def userInput():
    global x0, y0, x1, y1
    x0, y0, x1, y1 = input("Coordinates: ").split()
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Symmetric DDA")
    glutDisplayFunc(draw)
    init()
    userInput()
    glutMainLoop()

main()