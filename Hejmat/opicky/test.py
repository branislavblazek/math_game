import heapq

def dijkstra(graf, zac, kon):
    heap = []
    navs = [-1] * len(graf)
    
    heapq.heappush(heap, (0, zac))
    
    while heap:
        x = heapq.heappop(heap)

        vzdial = x[0]
        vrchol = x[1][0]
        
        if(navs[vrchol] != -1):
            continue
        
        navs[vrchol] = vzdial
            
        for i in range(0, len(graf[vrchol])):
            novy_vrchol = graf[vrchol][i]
            
            if(navs[novy_vrchol[0]] == -1):
                z = (vzdial+graf[vrchol][i][1], novy_vrchol)
                heapq.heappush(heap, z)

    return navs[kon[0]]

################################################################################

n, m = input().split()
n = int(n)
m = int(m)
    
graf = [ [] for i in range(n) ]
vahy = [ [] for i in range(n) ]

for i in range(m):
    a, b, w = input().split()
    a = int(a)
    b = int(b)
    w = int(w)
    
    a -= 1
    b -= 1
    
    graf[a].append([b, w])
    graf[b].append([a, w])

zac, kon = input().split()
zac = int(zac)
kon = int(kon)

zac -= 1
kon -= 1

print(graf)

print(dijkstra(graf, [zac,0], [kon,0]))