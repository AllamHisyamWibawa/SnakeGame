import OpenGL 
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

from Urgent import render

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

def timer(timer, value):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 0)

def keyboard(key, x, y):

    if key == b'a':
        glTranslatef(-50, -50, 0)
        drawingHome()
    if key == b'd':
        glTranslatef(50, -50, 0)
        drawingHome()
    if key == b'q':
        glTranslatef(-50, 50, 0)
        drawingHome()
    if key == b'e':
        glTranslatef(50, 50, 0)
        drawingHome()

    if key == b'z':
        glRotatef(50, 0, 0, 1)
        drawingHome()
    if key == b'x':
        glRotatef(-50, 0, 0, 1)
        drawingHome()
    if key == b'c':
        glRotatef(90, 0, 0, 1)
        drawingHome()

    glutPostRedisplay()

def spesial(key, x, y):
    if key == GLUT_KEY_UP:
        glTranslatef(0, 50, 0)
        drawingHome()
    if key == GLUT_KEY_DOWN:
        glTranslatef(0, -50, 0)
        drawingHome()
    if key == GLUT_KEY_LEFT:
        glTranslatef(-50, 0, 0)
        drawingHome()
    if key == GLUT_KEY_RIGHT:
        glTranslatef(50, 0, 0)
        drawingHome()

    glutPostRedisplay()

skala = 1
maxskala = 1.5

def mouse(button, state, x y):
    global skala
    global maxskala

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            glScalef(skala, skala, 0)
            drawingHome()
            if skala > maxskala:
                skala = 1
            else:
                skala = skala + 0.1
            return()
    
    if button == GLUT_RIGHT_BUTTON :
        if state == GLUT_DOWN:
            glScalef(skala, skala, 0)
            drawingHome()
            if skala > maxskala:
                skala = 1
            else:
                skala = skala - 0.1
            return()

    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Allam Hisyam Wibawa(202410103057) | Moch Rifky Noer Rachman(202410103048)")
    glutDisplayFunc(render)
    glutTimerFunc(50, timer, 0)
    init()
    glutMainLoop()

main()
