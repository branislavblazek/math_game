connections = (
        'A B', 'A F',
        'B G', 'B C',
        'C F', 'C H',
        'D H', 'D I',
        'E I', 'E J',
        'G H',
        'H I',
        'I J'
)
susedia = []
for connection in connections:
    start, to = connection.split(' ')

    pridajA = True
    pridajB = True

    for item in susedia:
        if item[0] == start:
            pridajA = False
            item.append(to)
        if item[0] == to:
            pridajB = False
            item.append(start)

    if pridajA:
        susedia.append([start, to])
    if pridajB:
        susedia.append([to, start])

print(susedia)