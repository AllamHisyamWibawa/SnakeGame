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
    glclearColor(, , , )
    gluOrtho2D(, , , )

def drawingHome():
    #Segitiga atap
    glColor3f(, , , )
    glBegin(GL_TRIANGLES)
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glEnd()

    #Dinding depan
    glColor3f(, , , )
    glBegin(GL_QUADS)
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glEnd()

    #Pintu
    glColor3f(, , , )
    glBegin(GL_QUADS)
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glEnd()

    #Dinding samping
    glColor3f(, , , )
    glBegin(GL_QUADS)
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glEnd()

    #Jendela
    glColor3f(, , , )
    glBegin(GL_QUADS)
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glEnd()

    #Atap
    glColor3f(, , , )
    glBegin(GL_QUADS)
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
    glVertex2i(, )
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
    if key == b'w':
        py -= 0.1
    if key == b's':
        py += 0.1

    if key == b'j':
        ax -= 10
    if key == b'l':
        ax += 10
    if key == b'i':
        ay -= 10
    if key == b'k':
        ay += 10

    if key == b'r':
        rx -= 45
    if key == b't':
        rx += 45
    if key == b'f':
        ry -= 45
    if key == b'g':
        ry += 45
    if key == b'v':
        rz -= 45
    if key == b'b':
        rz += 45
    glutPostRedisplay()

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(, , , )

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1200, 800)
    window = glutCreateWindow("Allam Hisyam Wibawa(202410103057) | Moch Rifky Noer Rachman(202410103048)")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

if __name__ == "__main__":
    main()
