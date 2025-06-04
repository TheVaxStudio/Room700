import sys
import pygame
from Settings import *
from Tilemap import Tilemap
from Camera import Camera
from Player import Player
from Light import Light

class Game:
    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)
        self.Clock = pygame.time.Clock()
        self.tilemap = Tilemap()
        self.light = Light()
        self.player = Player(self.tilemap)
        self.camera = Camera(128, 128)
        pygame.display.set_caption(Title)
        self.Render()

    def Render(self):
        self.Running = True
        while self.Running:
            self.Clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False
                    pygame.quit()
                    sys.exit()
            self.Screen.fill(Color)
            self.tilemap.draw(self.Screen, self.camera)
            self.light.draw(self.Screen)
            self.player.draw(self.Screen, self.camera)
            self.player.update()
            pygame.display.flip()