from zajo_game import zajo_level

level_max = 4
level_status = 1

while level_status <= level_max:
    action = zajo_level(level_status, level_max)
    if action == 'max':
        level_max += 1
    elif action == 'status':
        level_status += 1
