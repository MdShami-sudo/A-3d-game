import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, -1.5, -10)
glRotatef(25, 2, 1, 0)

black = (0, 0, 0)
white = (1, 1, 1)
gray = (0.5, 0.5, 0.5)
red = (1, 0, 0)

def draw_ground():
    glColor3fv(gray)
    glBegin(GL_QUADS)
    glVertex3f(-10, -1, 10)
    glVertex3f(10, -1, 10)
    glVertex3f(10, -1, -100)
    glVertex3f(-10, -1, -100)
    glEnd()

def draw_car(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3fv(red)
    glBegin(GL_QUADS)
    glVertex3f(-1, 0, 2)
    glVertex3f(1, 0, 2)
    glVertex3f(1, 0, -2)
    glVertex3f(-1, 0, -2)
    glVertex3f(-1, 1, 2)
    glVertex3f(1, 1, 2)
    glVertex3f(1, 1, -2)
    glVertex3f(-1, 1, -2)
    glVertex3f(-1, 0, 2)
    glVertex3f(-1, 1, 2)
    glVertex3f(1, 1, 2)
    glVertex3f(1, 0, 2)
    glVertex3f(-1, 0, -2)
    glVertex3f(-1, 1, -2)
    glVertex3f(1, 1, -2)
    glVertex3f(1, 0, -2)
    glEnd()
    glPopMatrix()

def draw_scene(car_x, car_y, car_z):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_ground()
    draw_car(car_x, car_y, car_z)
    pygame.display.flip()

def main():
    car_x, car_y, car_z = 0, 0, 0
    speed = 0.1

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            car_x -= speed
        if keys[K_RIGHT]:
            car_x += speed
        if keys[K_UP]:
            car_z -= speed
        if keys[K_DOWN]:
            car_z += speed

        draw_scene(car_x, car_y, car_z)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
