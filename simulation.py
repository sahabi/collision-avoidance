# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from time import sleep
from Controller_4 import Controller_4 as Ca_4
from pygame import Rect
import sys
from Queue import Queue

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (120, 78, 240)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)

def color_surface(surface, color):
    arr = pygame.surfarray.pixels3d(surface.src_image)
    arr[:,:,0] = color[0]
    arr[:,:,1] = color[1]
    arr[:,:,2] = color[2]

def dpos2pos(dpos):
    return (dpos[0]*450 + dpos[1]*45, dpos[2]*45)

def _collide(rect1, rect2):
    for layer1 in range(n_layers):
        for layer2 in range(n_layers):
            if Rect(rect1[layer1]).colliderect(Rect(rect2[layer2])):
                return True
            else:
                return False

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


class UAVSprite(pygame.sprite.Sprite):

    def __init__(self, dpos, color, display, ID, IDn, escape_point= (1, 1)):
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
        self.escape_point = escape_point

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

#fix this
    def setLayer(self, layer):
        self.set_dpos([0 if layer[6] == 'F' else 1, self.dpos[1], self.dpos[2]])

    def set_dpos(self, dpos, safe = True):
        if safe and self.in_region(dpos):
            self.dpos = dpos
            self.pos = dpos2pos(self.dpos)
        else:
           sys.quit()

    def in_region(self, dpos):
        return True

    def collide(self, uav):
        rect1 = [rect for rect in self.region_rect]
        rect2 = [rect for rect in uav.region_rect]
        return _collid(rect1, rect2)

    def collide(self, uav):
        for layer1 in range(n_layers):
            for layer2 in range(n_layers):
                if Rect(self.region_rect[layer1]).colliderect(Rect(uav.region_rect[layer2])):
                    return True
                else:
                    return False

    def region_intersects(self, point):
        for uav in theApp.uav_record.keys():
            uav_o = theApp.uav_record[uav]
            if self.ID == uav_o.ID:
                continue
            if self.collide(uav_o) and point[0] == uav_o.dpos[0]:
                return uav_o
        return False

    def _gotoPoint(self, point):
        path = self.get_path(point.dpos)
        for point in path:
            self.set_dpos(point)
            theApp.show()
            sleep(.1)

#fix this
    def gotoPoint(self, point):
        if point[4] == 'N':
            return
        point = theApp.point_record['point{}'.format(ord(point[4])-65)]
        self._gotoPoint(point)

    def get_path(self, dpos):
        xsteps = self.dpos[1] - dpos[1]
        ysteps = self.dpos[2] - dpos[2]
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

#fix this
    def setIntent(self, intent):
        app = theApp
        conflict = ""
        if intent[4] == 'N':
            return
        print ord(intent[4])-65
        point = app.point_record['point{}'.format(ord(intent[4])-65)]
        print intent[4]
        path = self.get_path(point.dpos)
        #self.path_region = self.make_path_regions(path)
        self.update_region(point.dpos)
        if self.region_intersects(point.dpos):
            conflict = "{}_{}".format(self.IDn,
                                      self.region_intersects(point.dpos).IDn)
        sleep(.1)
        return conflict

    def make_regions(self, dpos, path=False):
        buf = 20
        regions = []
        if not path:
            for layer in range(n_layers):
                x = layer*450 + (min(self.pos[0]%450, dpos[1]*45)) - buf
                y = min(self.pos[1], dpos[2]*45) - buf
                width = 2*buf + max(self.pos[0]%450, dpos[1]*45) -\
                (min(self.pos[0]%450, dpos[1]*45))
                length = 2*buf + max(self.pos[1], dpos[2]*45) - min(self.pos[1],
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
        self.update_region(self.dpos)

    def send_away(self, app):
        label = myfont.render('A',False,(0,0,0))
        escp = self.get_escape()
        escape_point = PointSprite((self.dpos[0],escp[0],
            escp[1]), 1, text=label)
        self.update_region(escape_point.dpos)
        self._gotoPoint(escape_point)

    def get_escape(self):
        point = escape_points.get()
        escape_points.put(point)
        if self.is_point_safe(point):
            return point
        else:
            self.get_escape()

    def is_point_safe(self, point):
        return True


    def update(self):
        for layer in range(len(self.region_rect)):
            if layer == self.dpos[0]:
                pygame.draw.rect(self.display, self.color, self.region_rect[layer], 2)
        self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        print self.dpos

    def update_region(self, dpos, color = None):
        self.region_rect = []
        regions = self.make_regions(dpos)
        for layer in range(n_layers):
            self.region_rect.append(regions[layer])
            self.region_rect[layer]
            if layer == self.dpos[0]:
                pygame.draw.rect(self.display, self.color, self.region_rect[layer], 2)
        theApp.show()

    def get_layer(self):
        return self.discrete[0]

class App:
    def __init__(self, n_uavs, n_layers, n_locations):
        self._running = True
        self.display = None
        self.n_uavs = n_uavs
        self.n_layers = n_layers
        self.n_locations = n_locations
        self.layers = []
        self.size = self.width, self.height = 1400, 700

    def on_init(self):
        self.make_env()
        pygame.display.flip()

#fix this
    def make_env(self):
        for i in range(self.n_layers):
            self.layers.append(myfont.render('Altitude Layer {}'.format(i),
                                             False, (0, 0, 0)))
        self.display = pygame.display.set_mode(self.size,
                                               pygame.HWSURFACE |
                                               pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.display.get_size())
        self.background = self.background.convert()
        self.background.fill((255, 255, 255))
        self._running = True
        self.display.fill((255, 255, 255))
        self.draw_alt_borders()
        rect = self.display.get_rect()
        self.uav_record = {}
        self.uavs = []
        for key, value in uavs.iteritems():
            uav_sprite = UAVSprite(value['init'], value['color'],
                                   self.display, value['label'], i)
            self.uav_record[key] = uav_sprite
            self.uavs.append(uav_sprite)

        self.uav_group = pygame.sprite.RenderPlain(self.uav_record.values())
        self.uav_group.update()
        self.uav_group.clear(self.display,self.background)
        self.uav_group.draw(self.display)

        self.points = []
        self.point_record = {}
        for i in range(n_locations):
            font = myfont.render('Location {}'.format(chr(i+65)), False, (0,0,0))
            point_sprite = PointSprite(locations[i], 1, font)
            self.points.append(point_sprite)
            self.point_record['point{}'.format(i)] = point_sprite
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
        self.draw_alt_borders()
        for i in range(n_locations):
            self.display.blit(self.points[i].text,
                              dpos2pos(self.points[i].dpos_text))
        for i in range(n_layers):
            self.display.blit(self.layers[i], (300,635))

    def draw_alt_borders(self):
        for i in range(1,n_layers):
            pygame.draw.line(self.display, (100, 100, 100),
                             [i*int(self.width/self.n_layers), 0],
                             [i*int(self.width/self.n_layers), self.height], 5)

    def resolve_conflicts(self, conflicts):
        for conflict in conflicts:
            if conflict is None:
                continue
            self.resolve_conflict(conflict)

    def resolve_conflict(self, conflict):
        fixes = []
        if len(conflict) > 0:
            main_uav = self.uav_record["uav{}".format(conflict[0])]
            temp_region = main_uav.region_rect
            main_uav.shrink_regions()
            second_uav = self.uav_record["uav{}".format(conflict[2])]
            fixes.append(second_uav.shrink_regions)
            fixes.append(second_uav.send_away)
            fixes.append(second_uav.shrink_regions)
            i = 0
            while(_collide(temp_region, second_uav.region_rect)):
                if i == 9:
                    sys.quit()
                fixes[i%2](self)
                i += 1
            main_uav.region_rect = temp_region

    def show(self):
        self.reset_map()
        self.point_group.update()
        self.point_group.clear(self.display,self.background)
        self.point_group.draw(self.display)
        self.uav_group.update()
        self.uav_group.clear(self.display,self.background)
        self.uav_group.draw(self.display)
        pygame.display.flip()
        sleep(0.1)

#fix this
    def plan_mission(self, ctrl_output):
        plan = {}
        for uav in self.uav_record.keys():
            plan[uav] = []
            plan[uav].append('{}'.format(ctrl_output[uav+"_intent"]))
            plan[uav].append('{}'.format(ctrl_output[uav+"_goto"]))
            plan[uav].append('{}'.format(ctrl_output[uav+"_layer"]))
        return plan

    def exec_plan(self, plan):
        conflicts = []
        for uav in self.uav_record.keys():
            self.uav_record[uav].setLayer(plan[uav][-1])
            plan[uav].pop()
            self.uav_record[uav].gotoPoint(plan[uav][-1])
            plan[uav].pop()
            conflicts.append(self.uav_record[uav].setIntent(plan[uav][-1]))
            plan[uav].pop()
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
            inputs = {}
            for i in range(n_uavs):
                for j in range(i,n_uavs):
                    if i != j:
                        inputs['uav{}_{}_collide'.format(i,j)] =\
                        self.uavs[i].collide(self.uavs[j])
            # getting the outputs out of the controller
            outputs = ctrl.move(**inputs)
            plan = self.plan_mission(outputs)
            self.exec_plan(plan)
            sleep(.1)

        self.on_cleanup()

if __name__ == "__main__" :
    n_uavs = 4
    n_layers = 3
    n_locations = 4

    keys = ['uav'+str(i) for i in range(n_uavs)]
    uav_props = {'init':None,'color':None,'label':None,'id':None}
    uavs = {key:{'init':None,'color':None,'label':None,'id':None} for key in keys}
    uavs['uav0']['init'] = (0, 2, 12)
    uavs['uav0']['color'] = BLACK
    uavs['uav0']['label'] = 'black'
    uavs['uav0']['id'] = 0
    uavs['uav1']['init'] = (1, 7, 2)
    uavs['uav1']['color'] = PURPLE
    uavs['uav1']['label'] = 'purple'
    uavs['uav1']['id'] = 1
    uavs['uav2']['init'] = (2, 2, 2)
    uavs['uav2']['color'] = GREEN
    uavs['uav2']['label'] = 'green'
    uavs['uav2']['id'] = 2
    uavs['uav3']['init'] = (2, 8, 8)
    uavs['uav3']['color'] = RED
    uavs['uav3']['label'] = 'red'
    uavs['uav3']['id'] = 3 
    locations = []
    locations.append((0,1,8))
    locations.append((1,8,2))
    locations.append((2,1,8))
    locations.append((2,1,2))

    pygame.init()
    pygame.font.init()

    myfont = pygame.font.SysFont('Comic Sans MS', 22)
    escape_points = Queue(maxsize=6)
    escape_points.put((1,1))
    escape_points.put((8,1))
    escape_points.put((5,5))
    escape_points.put((4,11))

    ctrl = Ca_4()
    theApp = App(n_uavs=4,n_layers=3,n_locations=4)
    theApp.on_execute()
