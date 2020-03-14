from opicky.opicky_game import opicky_level
import pygame as pg
import random

def opicky_main_func(pg, screen):
    level_max = 5
    level_status = 1

    while level_status < level_max:
        cislo = random.randint(0,5)
        cislo = 5
        action = opicky_level(pg, screen, level_status, level_max, cislo)
        if action == 1:
            level_status += 1
        elif action == 0:
            level_max += 1
        elif action == 2:
            break

    if level_status >= level_max:
        return 1
    else:
        return 0