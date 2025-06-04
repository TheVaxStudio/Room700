from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.math import Vector2

class Camera:
    def __init__(self, width, height):
        self.offset = Vector2(0, 0)
        self.position = [0, 0, 0]
        self.width = width
        self.height = height

    def apply(self, rect):
        return rect.move(self.offset.x, self.offset.y)

    def update(self, target):
        self.position[0] = target.rect.x + target.rect.width // 2 - self.width // 2
        self.position[1] = target.rect.y + target.rect.height // 2 - self.height // 2

    def apply_view(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.position[0], self.position[1], 1, self.position[0], self.position[1], 0, 0, 1, 0)