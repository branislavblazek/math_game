def all_connections():
    connections = [    
    (
        'A B', 'A F',
        'B G', 'B C',
        'C F', 'C H',
        'D H', 'D I',
        'E I', 'E J',
        'G H',
        'H I',
        'I J'
    ),
    (
        'A B', 'A F',
        'B G',
        'C G', 'C D', 'C H',
        'D I',
        'E J',
        'F G',
        'H E',
        'I J'
    ),
    (
        'A B', 'A F',
        'B F', 'B G',
        'C F', 'C D',
        'D H', 'D I',
        'E H', 'E J',
        'G H'
    ),
    (
        'A B', 'A F',
        'B C',
        'C F', 'C G', 'C H',
        'D G', 'D H', 'D I',
        'E H', 'E I', 'E J',
        'I J'
    ),
    (
        'A B', 'A F',
        'B C',
        'C G', 
        'D G', 'D H', 'D I',
        'E J', 'E I', 'E H',
        'F G',
        'G H',
        'I J'
    ),
    (
        'A B', 'A F',
        'B F', 'B G',
        'C F', 'C H',
        'D G', 'D E',
        'E I', 'E J',
        'H I',
        'I J'
    )
    ]
    return connections