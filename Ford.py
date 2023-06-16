import timeit

def Ford(graph, source):
    d = {v: float('inf') for v in graph}  # initialisation des distances à l'infini
    d[source] = 0  # distance à la source = 0
    for k in range(len(graph)):
        for u in graph:
            for v in graph[u]:
                w = graph[u][v]  # poids de l'arc (u, v)
                if d[u] + w < d[v]:  # s'il y a un chemin plus court que le courant
                    d[v] = d[u] + w  # mettre à jour la distance
    return d

# Test du programme
graph = {

    'A': {'B': 4, 'C': 1},
    'B': {'E': 4},
    'C': {'D': 3},
    'D': {'E': 1},
    'E': {}
}



# Appel de la fonction Ford avec le sommet de départ A
distances = Ford(graph, 'A')

# Affichage des distances les plus courtes à partir de A
print(distances)

# Mesure du temps d'exécution avec timeit
t = timeit.timeit(number=1) 
print("Durée d'exécution : %.5f secondes" % t)
