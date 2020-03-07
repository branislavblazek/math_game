from opicky.opicky_game import opicky_level
import pygame as pg

def opicky_main_func(pg, screen):
    level_max = 4
    level_status = 1

    while level_status < level_max:
        action = opicky_level(pg, screen, level_status, level_max)
        if action == 1:
            level_status += 1
        elif action == 0:
            level_max += 1
        elif action == 2:
            break