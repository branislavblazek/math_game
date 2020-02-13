from zabky.zabky_game import zabky_level
import pygame as pg
import random

def zabky_main_func(pg, screen):
    choices = {
        20: [9,11,8,6],
        19: [12,7,10,5],
        18: [2,9,13,5],
        17: [10,8,9,5],
        16: [7,9,8,6],
        15: [6,8,7,4],
        14: [9,5,7,3],
        13: [5,6,10,7],
        12: [7,5,4,6],
        11: [4,7,6,5],
        10: [6,3,4,5],
        9: [3,5,2,4],
        8: [2,5,3,6],
        7: [5,3,4,3],
        6: [4,1,2,3],
        5: [1,3,2,4]}

    choices2 = {}

    level_max = 4
    level_status = 1

    while level_status <= level_max:

        if len(choices2) == 0:
            choices2 = choices.copy()

        key, value = random.choice(list(choices2.items()))

        del choices2[key]
        random.shuffle(value)
        action = zabky_level(pg, screen, level_status, level_max, key, value)

        if action == 1:
            level_status += 1
        elif action == 0:
            level_max += 1
        elif action == 2:
            break
