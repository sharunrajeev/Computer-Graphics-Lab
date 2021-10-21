from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Declare Sign function
def Sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-100, 100, -100, 100)


def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)
    glPointSize(5.0)

    # Declare variables and initialise them
    x1, y1 = map(int, input("Enter (x1,y1) - ").split())
    x2, y2 = map(int, input("Enter (x2,y2) - ").split())
    x = x1
    y = y2
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = Sign(x2 - x1)
    s2 = Sign(y2 - y1)

    # Interchange dx and dy depending on slop
    if dx > dy:
        temp = dx
        dx = dy
        dy = temp
        ic = 1
    else:
        ic = 0
    
    # Initialise error term
    e = 2 * dy - dx

    for i in range(1, dx + 1):
        set_pixel(x, y)
        while e >= 0:
            if ic == 1:
                x += s1
            else:
                y += s2
            e -= 2 * dx
        if ic == 1:
            y += s2
        else:
            x += s1
        e += 2 * dy

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Bressenham's Line Drawing Algorithm")
    glutDisplayFunc(draw_line)
    init()
    glutMainLoop()


main()