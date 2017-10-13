# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from time import sleep
from Controller_4 import Controller_4 as Ca_4
from pygame import Rect

ctrl = Ca_4()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (120, 78, 240)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
LAYERS = 2
N_UAVS = 3
UAVS = []

for i in range(N_UAVS):
    UAVS.append('uav{}'.format(i+1))

def color_surface(surface, color):
    arr = pygame.surfarray.pixels3d(surface.src_image)
    arr[:,:,0] = color[0]
    arr[:,:,1] = color[1]
    arr[:,:,2] = color[2]

def return_input(uav1_2_collide, uav1_3_collide,
                uav2_3_collide):
    return {
        "uav1_2_collide": False,# uav1_2_collide,
        "uav1_3_collide": False,#uav1_3_collide,
        "uav2_3_collide": False,#uav2_3_collide,
    }

def dpos2pos(dpos):
    return (dpos[0]*450 + dpos[1]*45, dpos[2]*45)

class OpRegion(pygame.sprite.Sprite):
    def __init__(self, display, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = display
        self.rect = self.image.get_rect()

    def update(self,rect):
        self.image = pygame.Surface((rect[2], rect[3]))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (rect[0], rect[1])
        pygame.draw.rect(self.image, BLACK, rect, 5)

class PointSprite(pygame.sprite.Sprite):

    def __init__(self, dpos, label, text):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("assets/point.png")
        self.src_image = pygame.transform.scale(self.src_image,(25,25))
        self.label = label
        self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        self.dpos = dpos
        self.dpos_text = (dpos[0], dpos[1], dpos[2]+.5)
        self.rect.center = dpos2pos(dpos)
        self.text = text

    def update(self):
        pass

class UAVSprite(pygame.sprite.Sprite):

    def __init__(self, dpos, color, display):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("assets/uav.png")
        self.dpos = dpos
        self.pos = dpos2pos(dpos)
        arr = pygame.surfarray.pixels3d(self.src_image)
        arr[:,:,0] = color[0]
        arr[:,:,1] = color[1]
        arr[:,:,2] = color[2]
        self.color = color
        self.display = display
        self.operating_region = OpRegion(display, color)
        self.region_rect = []

    def move(self, action):
        l, x, y = self.dpos
        if action == 'east' and self.next_state[1] < 9:
            x += 1
        elif action == 'west' and self.next_state[1] > 1:
            x -= 1
        elif action == 'south' and self.next_state[2] < 15:
            y += 1
        elif action == 'north' and self.next_state[2] > 1:
            y -= 1
        self.set_dpos(l, x, y)

    def setLayer(self, layer):
        self.set_dpos([0 if layer[6] == 'F' else 1, self.dpos[1], self.dpos[2]])

    def set_dpos(self, dpos):
        self.dpos = dpos
        self.pos = dpos2pos(self.dpos)

    def collide(self, uav):
        return False

    def gotoPoint(self, point, app):
        if point[4] == 'N':
            return
        if point[4] == 'A':
            point = app.point_record['point1']
        elif point[4] == 'B':
            point = app.point_record['point2']
        path = self.get_path(point)
        for point in path:
            self.set_dpos(point)
            app.show()
            sleep(.2)

    def get_path(self, point):
        xsteps = self.dpos[1] - point.dpos[1]
        ysteps = self.dpos[2] - point.dpos[2]
        if xsteps < 0:
            xpoints = [self.dpos[1] + i + 1 for i in range(abs(xsteps))]
        elif xsteps > 0:
            xpoints = [self.dpos[1] - i - 1 for i in range(xsteps)]
        else:
            xpoints = [self.dpos[1]]
        if ysteps < 0:
            ypoints = [self.dpos[2] + i + 1 for i in range(abs(ysteps))]
        elif ysteps > 0:
            ypoints = [self.dpos[2] - i - 1 for i in range(ysteps)]
        else:
            ypoints = [self.dpos[2]]
        zpoints = [self.dpos[0]]*max(xsteps,ysteps)
        if abs(xsteps) > abs(ysteps):
            if ysteps == 1:
                ypoints = ypoints * (abs(xsteps)-abs(ysteps)+1)
            else:
                ypoints = ypoints[:-1] + [ypoints[-1]]*(abs(xsteps)-abs(ysteps)+1)
        else:
            xpoints = xpoints[:-1] + [xpoints[-1]]*(abs(ysteps)-abs(xsteps)+1)
        points = zip(zpoints, xpoints, ypoints)
        return points

    def setIntent(self, intent, app):
        if intent[4] == 'N':
            return
        if intent[4] == 'A':
            point = app.point_record['point1']
        elif intent[4] == 'B':
            point = app.point_record['point2']
        self.update_region(point, app)
        sleep(.2)

    def update(self):
        self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        for layer in range(len(self.region_rect)):
            pygame.draw.rect(self.display, self.color, self.region_rect[layer], 2)

    def update_region(self, dpos, app, color = None):
        self.region_rect = []
        for layer in range(LAYERS):
            self.region_rect.append([layer*450+self.pos[0]-20,self.pos[1]-20,100,100])
            pygame.draw.rect(self.display, self.color, self.region_rect[layer], 2)
        print self.region_rect

    def get_layer(self):
        return self.discrete[0]

    def get_pos(self):
        for pos in POS_LIST:
            if is_in(self.rect.center, pos.rect.center):
                return pos.label
        return 0

class App:
    def __init__(self):
        self._running = True
        self.display = None
        self.size = self.width, self.height = 900, 700

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.make_env()
        pygame.display.flip()

    def make_env(self):
        myfont = pygame.font.SysFont('Comic Sans MS', 22)
        self.layer_1 = myfont.render('Layer 1', False, (0, 0, 0))
        self.layer_2 = myfont.render('Layer 2', False, (0, 0, 0))
        self.display = pygame.display.set_mode(self.size,
                                               pygame.HWSURFACE |
                                               pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.display.get_size())
        self.background = self.background.convert()
        self.background.fill((255, 255, 255))
        self._running = True
        self.display.fill((255, 255, 255))
        pygame.draw.line(self.display, (100, 100, 100),
                         [int(self.width/LAYERS), 0],
                         [int(self.width/LAYERS), self.height], 5)
        rect = self.display.get_rect()

        self.uav_1 = UAVSprite((0, 1, 1), BLACK, self.display)
        self.uav_2 = UAVSprite((0, 1, 9), PURPLE, self.display)
        self.uav_3 = UAVSprite((1, 8, 3), GREEN, self.display)
        self.uav_record = {
            'uav1': self.uav_1,
            'uav2': self.uav_2,
            'uav3': self.uav_3
        }
        self.uav_group = pygame.sprite.RenderPlain(self.uav_record.values())
        self.uav_group.update()
        self.uav_group.clear(self.display,self.background)
        self.uav_group.draw(self.display)

        loc_a = myfont.render('Location A', False, (0, 0, 0))
        loc_b = myfont.render('Location B', False, (0, 0, 0))
        self.point_1 = PointSprite((0 , 1, 8), 1, loc_a)
        self.point_2 = PointSprite((1, 8, 2), 1, loc_b)
        self.point_record = {
            'point1': self.point_1,
            'point2': self.point_2
        }
        self.point_group = pygame.sprite.RenderPlain(self.point_record.values())
        self.point_group.update()
        self.point_group.clear(self.display,self.background)
        self.point_group.draw(self.display)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def reset_map(self):
        self.display.fill(pygame.Color("white"))
        pygame.draw.line(self.display, (100, 100, 100),
                         [int(self.width/LAYERS), 0],
                    [int(self.width/LAYERS), self.height], 5)
        self.display.blit(self.point_1.text, dpos2pos(self.point_1.dpos_text))
        self.display.blit(self.point_2.text, dpos2pos(self.point_2.dpos_text))
        self.display.blit(self.layer_1, (350,635))
        self.display.blit(self.layer_2, (800, 635))

    def resolve_conflict(self):
        pass

    def show(self):
        self.reset_map()
        self.uav_group.update()
        self.uav_group.clear(self.display,self.background)
        self.uav_group.draw(self.display)
        self.point_group.update()
        self.point_group.clear(self.display,self.background)
        self.point_group.draw(self.display)
        pygame.display.flip()
        sleep(0.5)

    def plan_mission(self, ctrl_output):
        plan = {
            "uav1" :[],
            "uav2" :[],
            "uav3" :[]
        }
        plan["uav3"].append('{}'.format(ctrl_output["uav3_intent"]))
        plan["uav2"].append('{}'.format(ctrl_output["uav2_intent"]))
        plan["uav1"].append('{}'.format(ctrl_output["uav1_intent"]))
        plan["uav3"].append('{}'.format(ctrl_output["uav3_goto"]))
        plan["uav2"].append('{}'.format(ctrl_output["uav2_goto"]))
        plan["uav1"].append('{}'.format(ctrl_output["uav1_goto"]))
        plan["uav3"].append('{}'.format(ctrl_output["uav3_layer"]))
        plan["uav2"].append('{}'.format(ctrl_output["uav2_layer"]))
        plan["uav1"].append('{}'.format(ctrl_output["uav1_layer"]))
        return plan

    def exec_plan(self, plan):
        for uav in UAVS:
            print("UAV: {}, Layer: {}".format(uav,plan[uav][-1]))
            self.uav_record[uav].setLayer(plan[uav][-1])
            plan[uav].pop()
            self.uav_record[uav].gotoPoint(plan[uav][-1], self)
            print("UAV: {}, Goto: {}".format(uav,plan[uav][-1]))
            plan[uav].pop()
            self.uav_record[uav].setIntent(plan[uav][-1], self)
            print("UAV: {}, Intent: {}".format(uav,plan[uav][-1]))
            plan[uav].pop()
            self.show()
        self.resolve_conflict()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)

            self.show()
            # creating inputs to controller
            uav1_2_collide = self.uav_1.collide(self.uav_2)
            uav1_3_collide = self.uav_1.collide(self.uav_3)
            uav2_3_collide = self.uav_2.collide(self.uav_3)
            inputs = return_input(uav1_2_collide, uav1_3_collide,
                                  uav2_3_collide)
            # getting the outputs out of the controller
            outputs = ctrl.move(**inputs)
            plan = self.plan_mission(outputs)
            self.exec_plan(plan)
            sleep(1)

        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
