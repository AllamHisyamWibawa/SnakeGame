import OpenGL
from OpenGL import GL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

px = 0.5
py = 0.5
ax = 0
ay = 0
rx = 0
ry = 0
rz = 0

def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)
    gluOrtho2D(0.0, 600.0, 0.0, 600.0)

def drawingHome():
    #Background
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.3, 0.0)

    #Dinding depan atas
    glColor3f(0.7, 0.2, 0.9)
    glBegin(GL_TRIANGLES)
    glVertex2i(20, 150)
    glVertex2i(100, 150)
    glVertex2i(50, 200)
    glEnd()

    #Dinding depan
    glColor3f(0.0, 0.0, 0.5)
    glBegin(GL_QUADS)
    glVertex2i(20, 20)
    glVertex2i(100, 20)
    glVertex2i(100, 150)
    glVertex2i(20, 150)
    glEnd()

    #Dinding kanan
    glColor3f(0.1, 0.2, 0.3)
    glBegin(GL_QUADS)
    glVertex2i(100, 20)
    glVertex2i(300, 20)
    glVertex2i(300, 150)
    glVertex2i(100, 150)
    glEnd()

    #Atap kanan
    glColor3f(1.0, 0.5, 2.0)
    glBegin(GL_QUADS)
    glVertex2i(100, 150)
    glVertex2i(300, 150)
    glVertex2i(250, 200)
    glVertex2i(60, 200)
    glEnd()

    #Pintu
    glColor3f(0.7, 0.2, 0.9)
    glBegin(GL_QUADS)
    glVertex2i(35, 20)
    glVertex2i(85, 20)
    glVertex2i(85, 100)
    glVertex2i(35, 100)
    glEnd()

    #Jendela kiri
    glColor3f(0.7, 0.2, 0.9)
    glBegin(GL_QUADS)
    glVertex2i(115, 50)
    glVertex2i(185, 50)
    glVertex2i(185, 100)
    glVertex2i(115, 100)
    glEnd()

    #Kisi jendela kiri
    glColor3f(1.0, 0.5, 2.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2i(150, 50)
    glVertex2i(150, 100)
    glVertex2i(115, 74)
    glVertex2i(185, 74)
    glEnd()

    #Jendela kanan
    glColor3f(0.7, 0.2, 0.9)
    glBegin(GL_QUADS)
    glVertex2i(215, 50)
    glVertex2i(285, 50)
    glVertex2i(285, 100)
    glVertex2i(215, 100)
    glEnd()

    #Kisi jendela kanan
    glColor3f(1.0, 0.5, 2.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2i(250, 50)
    glVertex2i(250, 100)
    glVertex2i(215, 74)
    glVertex2i(285, 74)
    glEnd()

def render():
    glPushMatrix()
    glTranslatef(ax, ay, 1)
    glScalef(px, py, 0)
    glRotate(45, rx, ry, rz)
    drawingHome()
    glPopMatrix()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    render()
    glutSwapBuffers()

    #Keyboard Code
def buttons(key, x, y):
    global px, py, ax, ay, rx, ry, rz
    if key == b'a':
        px -= 0.1
    if key == b'd':
        px += 0.1
    if key == b's':
        py -= 0.1
    if key == b'w':
        py += 0.1

    if key == b'j':
        ax -= 10
    if key == b'l':
        ax += 10
    if key == b'k':
        ay -= 10
    if key == b'i':
        ay += 10

    if key == b'r':
        rx += 40
    if key == b't':
        rx -= 40
    if key == b'f':
        ry += 40
    if key == b'g':
        ry -= 40
    if key == b'v':
        rz += 40
    if key == b'b':
        rz -= 40
    glutPostRedisplay()

def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)
    gluOrtho2D(0.0, 600.0, 0.0, 600.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1200, 800)
    glutCreateWindow("Allam Hisyam Wibawa(202410103057) | Moch Rifky Noer Rachman(202410103048)")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

if __name__ == "__main__":
    main()
