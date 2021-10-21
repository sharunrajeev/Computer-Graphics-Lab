# DDA for positive slope
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import log10, ceil  # For log

x0, y0 = 50, 50
xEnd, yEnd = 50, 200


def ROUND(a):
    return int(a + 0.5)


def myInit():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)


def readInput():
    global x0, y0, xEnd, yEnd
    print("Enter Coordinates (x1,y1) (x2,y2):", end=" ")
    x0, y0, xEnd, yEnd = map(int, input().split())


def setPixel(xcoordinate, ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate, ycoordinate)
    glEnd()
    glFlush()


def find_e(m):
    """
    Calculates value of n for e = 2^-n
    n > log(m)/log(2)
    """
    n = ceil(log10(m)/log10(2))

    return 2**(-n)


def lineSymmetricDDA(x1, y1, x2, y2):

    dx = x2-x1
    dy = y2-y1
    m = max(abs(dx), abs(dy))
    e = find_e(m)
    print(e)
    Xinc = float(dx*e)
    Yinc = float(dy*e)
    x, y = x0, y0
    setPixel(ROUND(x), ROUND(y))
    while round(x) != x2 or round(y) != y2:
        print("Pixels:", round(x), round(y))
        x += Xinc
        y += Yinc
        setPixel(ROUND(x), ROUND(y))
    print("Pixels:", round(x), round(y))  # Last pixel
    setPixel(ROUND(x), ROUND(y))  # Plot the last pixel


def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    lineSymmetricDDA(x0, y0, xEnd, yEnd)


def main():

    readInput()
    print("Starting window...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("DDA Line Algorithum")
    glutDisplayFunc(Display)
    myInit()
    glutMainLoop()


main()
