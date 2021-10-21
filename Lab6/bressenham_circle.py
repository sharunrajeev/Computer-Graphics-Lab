import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_circle():

    def mh(x, y, D):
        x = x+1
        D = D+(2*x)+1
        return x, y, D

    def md(x, y, D):
        x = x+1
        y = y-1
        D = D+(2*x)-(2*y)+2
        return x, y, D

    def mv(x, y, D):
        y = y-1
        D = D-(2*y)+1
        return x, y, D

    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)

    # Draw x axis and y axis
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(-1.0, 0.0)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)

    r = float(input("Radius = "))
    xc, yc = map(float, input("Center coordinates (x,y) = ").split(' '))

    x = 0.0
    y = r
    d = 2*(1-r)
    limit = 0
    v = 100
    while(y >= limit):
        glVertex2f((xc+x)/v, (yc+y)/v)
        glVertex2f((xc-x)/v, (yc+y)/v)
        glVertex2f((xc+x)/v, (yc-y)/v)
        glVertex2f((xc-x)/v, (yc-y)/v)
        glVertex2f((xc+y)/v, (yc+x)/v)
        glVertex2f((xc-y)/v, (yc+x)/v)
        glVertex2f((xc+y)/v, (yc-x)/v)
        glVertex2f((xc-y)/v, (yc-x)/v)

        if(d < 0):
            k1 = (2*d)+(2*y)-1
            if(k1 <= 0):
                x, y, d = mh(x, y, d)
            else:
                x, y, d = md(x, y, d)
        elif(d > 0):
            k2 = (2*d)-(2*x)-1
            if(k2 <= 0):
                x, y, d = md(x, y, d)
            else:
                x, y, d = mv(x, y, d)
        else:
            x, y, d = md(x, y, d)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(10, 10)
glutCreateWindow("Bressenham Incremental Circle")
glutDisplayFunc(draw_circle)
glutMainLoop()
