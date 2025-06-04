import pygame

class Animation:
    def __init__(self, spritesheet, frame_width, frame_height):
        self.spritesheet = spritesheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.animations = {
            'up': self.load_frames(0),
            'down': self.load_frames(1),
            'left': self.load_frames(2),
            'right': self.load_frames(3)
        }
        self.current_animation = 'down'
        self.current_frame = 0
        self.frame_duration = 100
        self.last_update = pygame.time.get_ticks()
        self.playing = False

    def load_frames(self, row):
        frames = []
        for col in range(self.spritesheet.get_width() // self.frame_width):
            frame = self.spritesheet.subsurface(pygame.Rect(
                col * self.frame_width,
                row * self.frame_height,
                self.frame_width,
                self.frame_height
            ))
            frames.append(frame)
        return frames

    def play(self, animation):
        if self.current_animation != animation:
            self.current_animation = animation
            self.current_frame = 0
            self.playing = True

    def stop(self):
        self.playing = False
        self.current_frame = 0

    def update(self):
        if self.playing:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_duration:
                self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
                self.last_update = now

    def get_current_frame(self):
        return self.animations[self.current_animation][self.current_frame]