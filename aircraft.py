#   File: aircraft.py

import math
import pygame
import os
import string
import conf
from waypoint import *
from utility import *
from game import *

class Aircraft:

    AC_IMAGE_NORMAL = pygame.image.load(os.path.join('data', 'aircraft.png'))
    AC_IMAGE_SELECTED = pygame.image.load(os.path.join('data', 'aircraft_sel.png'))
    AC_IMAGE_NEAR = pygame.image.load(os.path.join('data', 'aircraft_near.png'))

    AC_STATE_NORMAL = 1
    AC_STATE_SELECTED = 2
    AC_STATE_NEAR = 3

    EVENT_CLICK_AC = 0
    EVENT_CLICK_FS = 1
    
    FS_FONTSIZE = 18

	#Constructor!
    def __init__(self, game, location, speed, destination, ident):

        self.game = game

        #Game state vars
        self.lastEdit = 0
        self.location = location
        self.speed = speed
        self.altitude = 24000 # hardwired for now; measured in ft
        self.collisionRisk = []
        self.destination = destination.getLocation()
        self.ident = ident
        self.selected = False
        self.state = Aircraft.AC_STATE_NORMAL
        self.heading = self.__calculateHeading(self.location, self.destination)

        Aircraft.AC_IMAGE_NORMAL.convert_alpha()
        Aircraft.AC_IMAGE_SELECTED.convert_alpha()

        #Image/font vars
        self.image = Aircraft.AC_IMAGE_NORMAL
        self.font = pygame.font.Font(None, Aircraft.FS_FONTSIZE)
        self.fs_font_color = (255, 255, 255)
    
    #Return current location
    def getLocation(self):
        return self.location

    #Return current heading
    def getHeading(self):
        ret = 0
        if self.heading < 0:
            ret = 360 + self.heading
        else:
            ret = self.heading
        return ret
    
    def setHeading(self, newHeading):
        self.heading = newHeading

    def resetHeading(self):
        self.heading = self.__calculateHeading(self.location, self.destination)

    def checkHeading(self):
        return self.heading == self.__calculateHeading(self.location, self.destination)

    
    def turnHeading(self, angle):
        self.heading += 360 + angle
        self.heading %= 360
        
    def getHeadingStr(self):
        hdg = str(self.getHeading())
        hdg_str = hdg.split(".")[0]
        return hdg_str
        
    def getIdent(self):
        return self.ident

    def getSpeed(self):
        return self.speed

	#Set speed in pixels per frame
    def setSpeed(self, newspeed):
        self.speed = newspeed

    #Set whether I am the selected aircraft or not
    def setSelected(self, selected):
        self.selected = selected
        if(selected == True):
            self.image = Aircraft.AC_IMAGE_SELECTED
            self.fs.select()
        else:
            self.image = Aircraft.AC_IMAGE_NORMAL
            self.fs.deselect()
            
    def requestSelected(self):
        self.game.requestSelected(self)

	#Draw myself on the screen at my current position and heading
    def draw(self, surface):
        rot_image = pygame.transform.rotate(self.image, -self.heading)
        rect = rot_image.get_rect()
        rect.center = self.location
        surface.blit(rot_image, rect)

        if(conf.get()['aircraft']['draw_radius'] == True):
            pygame.draw.circle(surface, (255, 255, 0), self.location, conf.get()['aircraft']['collision_radius'], 1)

        #Draw lines and  if selected
        if(self.selected == True):
            point_list = []
            point_list.append(self.location)
            point_list.append(self.destination)
            pygame.draw.lines(surface, (255, 255, 0), False, point_list)

		# Draw the ident string next to the aircraft?
        x = self.location[0] + 20
        y = self.location[1]
        list = [self.ident, "FL" + str(self.altitude/100), str(self.speed) + "kts"]
        for line in list:
            id = self.font.render(line, False, self.fs_font_color)
            r = surface.blit(id, (x,y))
            y = y + self.font.get_height()

	#Location/heading update function
    def update(self):
        if(self.__reachedDestination(self.location, self.destination)):
            return True
		
        # self.heading = self.__calculateHeading(self.location, self.destination)
        self.location = self.__calculateNewLocation(self.location, self.heading, self.speed)
        self.fs.updateAllFields()

    def getClickDistanceSq(self, clickpos):
        return Utility.locDistSq(clickpos, self.location)
        
    def setFS(self, fs):
        self.fs = fs
        
    def getFS(self):
        return self.fs

    def __calculateHeading(self, location, waypoint):
        x_diff = waypoint[0] - location[0]
        y_diff = waypoint[1] - location[1]
		# Heading measured in degrees relative to North direction
        heading = math.degrees(math.atan2(y_diff, x_diff) + (math.pi / 2))
        return heading

	#Calculate new location based on current location, heading and speed
    def __calculateNewLocation(self, location, heading, speed):
        x_diff = (speed / conf.get()['aircraft']['speed_scalefactor']) * math.sin(math.radians(heading))
        y_diff = -(speed / conf.get()['aircraft']['speed_scalefactor']) * math.cos(math.radians(heading))
        location = (location[0] + x_diff, location[1] + y_diff)
        return location

    def __reachedDestination(self, location, waypoint):
        if Utility.locDistSq(location, waypoint) < ((self.speed/conf.get()['aircraft']['speed_scalefactor']) ** 2):
            return True
        else:
            return False

    def click(self, clickpos):
        if(Utility.locDistSq(clickpos, self.location) <= 100):
            return True
        else:
            return False
