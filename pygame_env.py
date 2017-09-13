# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from time import sleep


class PointSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.discrete = ()
        self.chosen = False

    def update(self, deltat):
        if self.chosen:
            color_surface(self, PURPLE)
            self.image = pygame.transform.rotate(self.src_image, 0)
        else:
            color_surface(self, BLACK)
            self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.position[1:]

    def select(self):
        self.chosen = True

    def unselect(self):
        self.chosen = False

class UAVSprite(pygame.sprite.Sprite):
    MAX_SPEED = 45
    TURN_SPEED = 5

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.next_state = (position[0]+(position[1]/450), (position[1]%450)/45, position[2]/45) 
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0
        self.discrete = self.next_state

    def move(self, action):
        l, x, y = self.next_state
        if action == 'east' and self.next_state[1] < 9:
            x += 1
        elif action == 'west' and self.next_state[1] > 1:
            x -= 1
        elif action == 'south' and self.next_state[2] < 15:
            y += 1
        elif action == 'north' and self.next_state[2] > 1:
            y -= 1
        elif action == 'ascend' and self.next_state[0] < 3:
            l += 1
            x += 0
            y += 0
        elif action == 'descend' and self.next_state > 0:
            l -= 1
            x = 0
            y = 0
        self.next_state = (l, x, y)

    def update(self, deltat):
        x = self.next_state[1] * 45 + (450 * self.next_state[0])
        y = self.next_state[2] * 45
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.discrete = self.next_state

def color_surface(surface, color):
    arr = pygame.surfarray.pixels3d(surface.src_image)
    arr[:,:,0] = color[0]
    arr[:,:,1] = color[1]
    arr[:,:,2] = color[2]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (120, 78, 240)

class App:
    def __init__(self):
        self._running = True
        self.display = None
        self.size = self.width, self.height = 1350, 700
        self.layers = 3

    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.display.get_size())
        self.background = self.background.convert()
        self.background.fill((255, 255, 255))
        self._running = True
        self.display.fill((255, 255, 255))
        pygame.draw.line(self.display, (100, 100, 100), [int(self.width/self.layers), 0],
                         [int(self.width/self.layers), self.height], 5)
        pygame.draw.line(self.display, (100, 100, 100),
                         [2*int(self.width/self.layers), 0],
                         [2*int(self.width/self.layers), self.height], 5)
        rect = self.display.get_rect()
        self.uav_1 = UAVSprite('assets/uav_1.png', (0 , 45, 45))
        self.uav_2 = UAVSprite('assets/uav_2.png', (0, rect.center[0],
                                                    rect.center[1]))
        self.point_1 = PointSprite('assets/uav_1.png', (0 , 90, 90))
        color_surface(self.uav_2, PURPLE)
        self.uav_group = pygame.sprite.RenderPlain((self.uav_1, self.uav_2))
        self.point_group = pygame.sprite.RenderPlain((self.point_1))
        self.layers = 3
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            sleep(1)
            self.uav_group.update(1)
            self.uav_group.clear(self.display,self.background)
            self.uav_group.draw(self.display)
            self.point_group.update(1)
            self.point_group.clear(self.display,self.background)
            self.point_group.draw(self.display)
            pygame.display.flip()
            self.uav_1.move('north')
            self.uav_2.move('west')
            self.point_1.select()
            print self.uav_2.discrete
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
