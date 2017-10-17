# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from time import sleep
from Controller_4 import Controller_4 as Ca_4
from pygame import Rect
import sys

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
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 22)

for i in range(N_UAVS):
    UAVS.append('uav{}'.format(i))

def color_surface(surface, color):
    arr = pygame.surfarray.pixels3d(surface.src_image)
    arr[:,:,0] = color[0]
    arr[:,:,1] = color[1]
    arr[:,:,2] = color[2]

def return_input(uav1_2_collide, uav1_3_collide,
                uav2_3_collide):
    return {
        "uav1_2_collide": uav1_2_collide,
        "uav1_3_collide": uav1_3_collide,
        "uav2_3_collide": uav2_3_collide,
    }

def dpos2pos(dpos):
    return (dpos[0]*450 + dpos[1]*45, dpos[2]*45)

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

    def __str__(self):
        return "{}, {}, {} ".format(self.dpos, self.text, self.label)

    __repr__ = __str__

loc_e = myfont.render('E', False, (0, 0, 0))
escape_point = PointSprite((1, 0, 0), 0, loc_e)

class UAVSprite(pygame.sprite.Sprite):

    def __init__(self, dpos, color, display, ID, IDn):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("assets/uav.png")
        self.dpos = dpos
        self.ID = ID
        self.IDn = IDn
        self.pos = dpos2pos(dpos)
        arr = pygame.surfarray.pixels3d(self.src_image)
        arr[:,:,0] = color[0]
        arr[:,:,1] = color[1]
        arr[:,:,2] = color[2]
        self.color = color
        self.display = display
        self.region_rect = self.make_regions(self.dpos)
        self.path_region = []
        esc_label = myfont.render(ID, False, (0,0,0))
        self.escape_point = (5, 9)

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

    def set_dpos(self, dpos, safe = True):
        if safe and self.in_region(dpos):
            self.dpos = dpos
            self.pos = dpos2pos(self.dpos)
        else:
            print("FAIL")

    def in_region(self, dpos):
        return True

    def collide(self, uav):
        for layer1 in range(LAYERS):
            for layer2 in range(LAYERS):
                if Rect(self.region_rect[layer1]).colliderect(Rect(uav.region_rect[layer2])):
                    return True
                else:
                    return False

    def region_intersects(self, app):
        for uav in UAVS:
            uav_o = app.uav_record[uav]
            if self.ID == uav_o.ID:
                continue
            if self.collide(uav_o):
                return uav_o
        return False

    def _gotoPoint(self, point, app):
        print("the point", point)
        path = self.get_path(point.dpos)
        print("the path", path)
        for point in path:
            self.set_dpos(point)
            app.show()
            sleep(.1)

    def gotoPoint(self, point, app):
        if point[4] == 'N':
            return
        if point[4] == 'A':
            point = app.point_record['point1']
        elif point[4] == 'B':
            point = app.point_record['point2']
        self._gotoPoint(point, app)

    def get_path(self, dpos):
        xsteps = self.dpos[1] - dpos[1]
        ysteps = self.dpos[2] - dpos[2]
        print(xsteps,ysteps)
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
        zpoints = [self.dpos[0]]*max(abs(xsteps),abs(ysteps))
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
        conflict = ""
        if intent[4] == 'N':
            return
        if intent[4] == 'A':
            point = app.point_record['point1']
        elif intent[4] == 'B':
            point = app.point_record['point2']
        path = self.get_path(point.dpos)
        self.path_region = self.make_path_regions(path)
        self.update_region(point.dpos, app)
        if self.region_intersects(app):
            conflict = "{}_{}".format(self.IDn, self.region_intersects(app).IDn)
            print("FAIL: UAV {} intersects with {}".format(self.ID,
                self.region_intersects(app).ID))
        sleep(.1)
        return conflict

    def make_regions(self, dpos):
        regions = []
        for layer in range(LAYERS):
            x = layer*450 + (min(self.pos[0]%450, dpos[1]*45)) - 30
            y = min(self.pos[1], dpos[2]*45) - 30
            width = 60 + max(self.pos[0]%450, dpos[1]*45) - (min(self.pos[0]%450, dpos[1]*45))
            length = 60 + max(self.pos[1], dpos[2]*45) - min(self.pos[1],
                    dpos[2]*45)
            regions.append([x, y, width, length])
        return regions

    def make_path_regions(self, path):
        regions = []
        for point in path:
            regions.append(self.make_unit_region(point))
        return regions


    def make_unit_region(self, dpos):
        return [dpos[0]*450+dpos[1]*45 - 30, dpos[2]*45 - 30, 60, 60]

    def shrink_regions(self, app=None):
        self.region_rect = self.make_regions(self.dpos)

    def send_away(self, app):
        print("sending away")
        label = myfont.render('A',False,(0,0,0))
        escape_point = PointSprite((self.dpos[0],self.escape_point[0],
            self.escape_point[1]), 1, text=label)
        self._gotoPoint(escape_point, app)

    def update(self):
        for layer in range(len(self.region_rect)):
            pygame.draw.rect(self.display, self.color, self.region_rect[layer], 2)
        #for region in self.path_region:
        #    pygame.draw.rect(self.display, self.color,
        #            region, 2)
        self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update_region(self, dpos, app, color = None):
        self.region_rect = []
        regions = self.make_regions(dpos)
        for layer in range(LAYERS):
            self.region_rect.append(regions[layer])
            self.region_rect[layer]
            pygame.draw.rect(self.display, self.color, self.region_rect[layer], 2)

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
        self.make_env()
        pygame.display.flip()

    def make_env(self):
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

        self.uav_0 = UAVSprite((0, 7, 12), BLACK, self.display, "black", 0)
        self.uav_1 = UAVSprite((0, 2, 12), PURPLE, self.display, "purple", 1)
        self.uav_2 = UAVSprite((1, 8, 3), GREEN, self.display, "green", 2)
        self.uav_record = {
            'uav0': self.uav_0,
            'uav1': self.uav_1,
            'uav2': self.uav_2
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

    def resolve_conflicts(self, conflicts):
        for conflict in conflicts:
            if conflict is None:
                continue
            self.resolve_conflict(conflict)

    def resolve_conflict(self, conflict):
        fixes = []
        if len(conflict) > 0:
            main_uav = self.uav_record["uav{}".format(conflict[0])]
            second_uav = self.uav_record["uav{}".format(conflict[2])]
            fixes.append(second_uav.shrink_regions)
            fixes.append(second_uav.send_away)
            i = 0
            while(main_uav.collide(second_uav)):
                if i == 6:
                    sys.quit()
                fixes[i%2](self)
                i += 1

    def show(self):
        self.reset_map()
        self.uav_group.update()
        self.uav_group.clear(self.display,self.background)
        self.uav_group.draw(self.display)
        self.point_group.update()
        self.point_group.clear(self.display,self.background)
        self.point_group.draw(self.display)
        pygame.display.flip()
        sleep(0.1)

    def plan_mission(self, ctrl_output):
        plan = {
            "uav0" :[],
            "uav1" :[],
            "uav2" :[]
        }
        plan["uav2"].append('{}'.format(ctrl_output["uav3_intent"]))
        plan["uav1"].append('{}'.format(ctrl_output["uav2_intent"]))
        plan["uav0"].append('{}'.format(ctrl_output["uav1_intent"]))
        plan["uav2"].append('{}'.format(ctrl_output["uav3_goto"]))
        plan["uav1"].append('{}'.format(ctrl_output["uav2_goto"]))
        plan["uav0"].append('{}'.format(ctrl_output["uav1_goto"]))
        plan["uav2"].append('{}'.format(ctrl_output["uav3_layer"]))
        plan["uav1"].append('{}'.format(ctrl_output["uav2_layer"]))
        plan["uav0"].append('{}'.format(ctrl_output["uav1_layer"]))
        return plan

    def exec_plan(self, plan):
        conflicts = []
        for uav in UAVS:
            self.uav_record[uav].setLayer(plan[uav][-1])
            plan[uav].pop()
            self.uav_record[uav].gotoPoint(plan[uav][-1], self)
            plan[uav].pop()
            conflicts.append(self.uav_record[uav].setIntent(plan[uav][-1],
                self))
            plan[uav].pop()
            self.show()
        if len(conflicts)>0:
            self.resolve_conflicts(conflicts)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)

            self.show()
            # creating inputs to controller
            uav0_1_collide = self.uav_0.collide(self.uav_1)
            uav0_2_collide = self.uav_0.collide(self.uav_2)
            uav1_2_collide = self.uav_1.collide(self.uav_2)
            inputs = return_input(uav0_1_collide, uav0_2_collide,
                                  uav1_2_collide)
            # getting the outputs out of the controller
            outputs = ctrl.move(**inputs)
            plan = self.plan_mission(outputs)
            self.exec_plan(plan)
            sleep(.1)

        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
