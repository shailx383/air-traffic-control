#!/usr/bin/env python
#   File: main.py

from pygame import *
from game import *
from highs import *
import os
import info_logger
import menu_base
import conf

STATE_MENU = 1
STATE_GAME = 2
STATE_DEMO = 3
STATE_HIGH = 4
STATE_KILL = 5
STATE_AGES = 6

class Main:

    BG_COLOR = (0, 0, 0)

    def __init__(self):
        #Init the modules we need
        display.init()
        pygame.mixer.init()
        font.init()
        
        if(conf.get()['game']['fullscreen'] == True):
            self.screen = display.set_mode((1024, 768), pygame.FULLSCREEN)
        else:
            self.screen = display.set_mode((1024, 768))
            
        display.set_caption('ATC Version 2')

        self.menu = menu_base.menu_base(self.screen,150,25)
        self.menu.from_file('main_menu')
        self.ages = menu_base.menu_base(self.screen,150,25)
        self.ages.from_file('ages_menu')
        self.high = HighScore(self.screen)
        self.infologger = info_logger.info_logger()
        #Current visitor number
        self.id = int(self.infologger.get_id())

    def run(self):
        state = STATE_MENU
        exit = 0
        score = 0

        while (exit == 0):
            if (state == STATE_MENU):
                menuEndCode = None
                menuEndCode = self.menu.main_loop()
                self.infologger.writeout()
                if (menuEndCode == conf.get()['codes']['start']):
                    state = STATE_AGES
                elif (menuEndCode == conf.get()['codes']['demo']):
                    state = STATE_DEMO
                elif (menuEndCode == conf.get()['codes']['high_score']):
                    state = STATE_HIGH
                elif (menuEndCode == conf.get()['codes']['kill']):
                    state = STATE_KILL
            elif (state == STATE_GAME):
                game = Game(self.screen, False)
                (gameEndCode,time, score) = game.start(self.agent)
                if (gameEndCode == conf.get()['codes']['time_up']):
                    state = STATE_HIGH
                elif (gameEndCode == conf.get()['codes']['kill']):
                    state = STATE_KILL
                elif (gameEndCode == conf.get()['codes']['user_end']):
                    state = STATE_MENU
                elif (gameEndCode == conf.get()['codes']['ac_collide']):
                    self.high.addSub(score,self.agent,time)
                    self.id += 1
                    self.infologger.add_value(self.id,'id',self.id)
                    self.infologger.add_value(self.id,'agent',self.agent)
                    self.infologger.add_value(self.id,'time',time)
                    self.infologger.add_value(self.id,'score',score)
                    self.infologger.writeout()
                    score=0
                    state = STATE_GAME
            elif (state == STATE_DEMO):
               game = Game(self.screen, True)
               (gameEndCode,time, score) = game.start(self.agent)
               state = STATE_MENU
            elif (state == STATE_HIGH):
                self.high.start()
                state = STATE_MENU
            elif (state == STATE_KILL):
                exit = 1
            elif (state == STATE_AGES):
                self.agent = self.ages.main_loop()
                state = STATE_GAME
            game = None

if __name__ == '__main__':
    game_main = Main()
    game_main.run()
