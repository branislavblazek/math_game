from krokovanie.zajo_game import zajo_level
from krokovanie.consts import Consts_game

def zajo_main_func(pg, screen):
    level_max = 5
    level_status = 1

    while level_status < level_max:
        action = zajo_level(pg, screen, level_status, level_max)
        if action == 'max':
            level_max += 1
        elif action == 'status':
            level_status += 1
        elif action == 2:
            break

    if level_status >= level_max:
        return 1
    else:
        return 0
