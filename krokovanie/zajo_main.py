from zajo_game import *
from consts import Consts_game
import pygame as pg

pg.init()
screen = pg.display.set_mode((const['window'].WIDTH, const['window'].HEIGHT))
pg.display.set_caption(const['window'].TITLE)

level_max = 4
level_status = 1

while level_status <= level_max:
    action = zajo_level(pg, screen, level_status, level_max)
    if action == 'max':
        level_max += 1
    elif action == 'status':
        level_status += 1
