import sys
import pygame
from Settings import settings as stg
from Tilemap import Tilemap
from Camera import Camera
from Player import Player
from Light import Light

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((stg['screen_width'], stg['screen_height']), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.tilemap = Tilemap()
        self.light = Light()
        self.player = Player(self.tilemap)
        self.camera = Camera(128, 128)
        pygame.display.set_caption(stg['title']) 
        self.loop()    

    def loop(self):
        self.running = True
        self.elapsed_frames = 0
        while self.running:
            self.update()
            self.render()                            

    def update(self):
        self.clock.tick(stg['fps'])
        self.elapsed_frames = (self.elapsed_frames + 1) % stg['fps']
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()                    
        self.player.update(self.elapsed_frames)

    def render(self):        
        self.screen.fill(stg['light']['color'])
        self.tilemap.draw(self.screen, self.camera)
        self.light.draw(self.screen)
        self.player.draw(self.screen, self.camera)
        pygame.display.flip()
        
            