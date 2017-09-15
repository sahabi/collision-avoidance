# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from time import sleep
from Ca_4 import Ca_4
ctrl = Ca_4()

print ctrl.move(0, 0, 0, False, False, False, 0, 0, 1)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (120, 78, 240)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)

POS_LIST = []
N_LAYERS = 2

def is_collide(uav1, uav2):
    return False

def is_in(loc1, loc2):
    if abs(loc1[0] - loc2[0]) < 50 and abs(loc1[1] - loc2[1]) < 50:
        return True
    else:
        return False

def make_rect(initial, destination):
    if initial[0] < destination[0]:
        x = initial[0] - 10
    else:
        x = destination[0] - 10

    if initial[1] < destination[1]:
        y = initial[1] - 10
    else:
        y = destination[1] - 10
    w = abs(initial[0] - destination[0]) + 60
    l = abs(initial[1] - destination[1]) + 60
    return pygame.Rect(x, y, w, l)


class Circle(pygame.sprite.Sprite):
    def __init__(self, display, color, init_rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = display
        self.rect = self.image.get_rect()

    def update(self,rect):
        self.image = pygame.Surface((rect[2], rect[3]))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (rect[0], rect[1])
        pygame.draw.rect(self.image, BLACK, rect, 5)


class RegionSprite(pygame.sprite.Sprite):

    def __init__(self, display, position, rect):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.Surface((500,500))
        self.color = BLACK
        self.surface = display
        self.rect = self.surface.get_rect()
        pygame.draw.rect(self.surface, self.color, self.rect)

    def update(self, rect):
        self.rect.center = self.position

class PointSprite(pygame.sprite.Sprite):

    def __init__(self, position, label):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("assets/point.png")
        self.src_image = pygame.transform.scale(self.src_image,(25,25))
        self.position = position
        self.chosen = False
        self.label = label

    def update(self):
        if self.chosen:
            color_surface(self, RED)
            self.image = pygame.transform.rotate(self.src_image, 0)
        else:
            color_surface(self, BLACK)
            self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0]*450 + self.position[1],
                            self.position[2])

    def select(self):
        self.chosen = True

    def unselect(self):
        self.chosen = False

class UAVSprite(pygame.sprite.Sprite):
    MAX_SPEED = 45
    TURN_SPEED = 5

    def __init__(self, position, color, display):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("assets/uav.png")
        self.position = position
        self.next_state = (position[0]+(position[1]/450), (position[1]%450)/45, position[2]/45)
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0
        self.discrete = self.next_state
        arr = pygame.surfarray.pixels3d(self.src_image)
        arr[:,:,0] = color[0]
        arr[:,:,1] = color[1]
        arr[:,:,2] = color[2]
        self.color = color
        self.display = display
        self.region_rect = (0,0,0,0)


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
        elif action == 'ascend' and self.next_state[0] < N_LAYERS:
            l += 1
            x += 0
            y += 0
        elif action == 'descend' and self.next_state > 0:
            l -= 1
            x = 0
            y = 0
        self.next_state = (l, x, y)

    def update(self):
        x = self.next_state[1] * 45 + (450 * self.next_state[0])
        y = self.next_state[2] * 45
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.discrete = self.next_state

    def update_region(self, point, color = None):
        if point.position[0] == self.discrete[0]:
            initial = self.position
            rect = make_rect(initial,[point.position[0]*450+ point.position[1],
                           point.position[2]])
            if color is not None:
                pygame.draw.rect(self.display, color, rect, 2)
            else:
                pygame.draw.rect(self.display, self.color, rect, 2)
            self.region_rect = rect

    def get_layer(self):
        return self.discrete[0]

    def get_pos(self):
        for pos in POS_LIST:
            if is_in(self.rect.center, pos.rect.center):
                return pos.label
        return 0

def color_surface(surface, color):
    arr = pygame.surfarray.pixels3d(surface.src_image)
    arr[:,:,0] = color[0]
    arr[:,:,1] = color[1]
    arr[:,:,2] = color[2]

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
        self.uav_1 = UAVSprite((0 , 45, 45), BLACK, self.display)
        self.uav_2 = UAVSprite((0, rect.center[0], rect.center[1]), PURPLE,
                               self.display)
        self.uav_3 = UAVSprite((1, 45, 80), GREEN, self.display)

        self.point_1 = PointSprite((0 , 90, 90), 'A')
        self.point_2 = PointSprite((0 , 190, 90), 'B')
        self.point_3 = PointSprite((1 , 45, 90), 'C')
        self.point_4 = PointSprite((1, 400, 200), 'D')

        POS_LIST.append(self.point_1)
        POS_LIST.append(self.point_2)
        POS_LIST.append(self.point_3)
        POS_LIST.append(self.point_4)
        self.operating_region_1 = Circle(self.display, BLACK, (100,100,200,200))
        self.region_group = pygame.sprite.RenderPlain((self.operating_region_1))
        self.uav_group = pygame.sprite.RenderPlain((self.uav_1, self.uav_2,
                                                    self.uav_3))
        self.point_group = pygame.sprite.RenderPlain((self.point_1,
                                                      self.point_2,
                                                      self.point_3,
                                                      self.point_4))
        self.layers = 3
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def reset_map(self):
        self.display.fill(pygame.Color("white"))
        pygame.draw.line(self.display, (100, 100, 100), [int(self.width/self.layers), 0],
                    [int(self.width/self.layers), self.height], 5)
        pygame.draw.line(self.display, (100, 100, 100),
                    [2*int(self.width/self.layers), 0],
                    [2*int(self.width/self.layers), self.height], 5)


    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)

            sleep(1)
            self.reset_map()

            self.uav_group.update()
            self.uav_group.clear(self.display,self.background)
            self.uav_group.draw(self.display)

            self.point_group.update()
            self.point_group.clear(self.display,self.background)
            self.point_group.draw(self.display)

            #self.uav_1.update_region(self.point_1)
            #self.uav_2.update_region(self.point_3)

            #self.uav_2.move('east')
            #self.uav_1.move('east')
            uav1_pos = self.uav_1.get_pos()
            uav2_pos = self.uav_2.get_pos()
            uav3_pos = self.uav_3.get_pos()
            uav1_2_collide = is_collide(self.uav_1, self.uav_2)
            uav1_3_collide = is_collide(self.uav_1, self.uav_3)
            uav2_3_collide = is_collide(self.uav_2, self.uav_3)
            uav1_layer = self.uav_1.get_layer()
            uav2_layer = self.uav_2.get_layer()
            uav3_layer = self.uav_3.get_layer()
            print (uav1_pos, uav2_pos, uav3_pos, uav1_2_collide,
                   uav1_3_collide, uav2_3_collide, uav1_layer, uav2_layer,
                   uav3_layer)
            pygame.display.flip()

        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
