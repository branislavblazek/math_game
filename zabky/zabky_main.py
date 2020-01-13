
from zabky_game import *
import pygame as pg

pg.init()
screen = pg.display.set_mode((const['window'].WIDTH, const['window'].HEIGHT))
pg.display.set_caption(const['window'].TITLE)

action = zabky_level(pg, screen, 1)
