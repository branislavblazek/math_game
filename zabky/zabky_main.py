from zabky.zabky_game import zabky_level
import pygame as pg

def zabky_main_func(pg, screen):
    action = zabky_level(pg, screen, 1, 5)
    print(action)
