from zabky.zabky_game import zabky_level
import pygame as pg

def zabky_main_func(pg, screen):
    level_max = 4
    level_status = 1

    while level_status <= level_max:
        action = zabky_level(pg, screen, level_status, level_max)
        if action == 1:
            level_status += 1
        elif action == 0:
            level_max += 1
