edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 2),
    (5, 1),
    (5, 4),
    (4, 6),
]
V = 7
graph = [[] for _ in range(V)]
for edge in edges:
   u, v = edge
   graph[u].append(v)
   graph[v].append(u)
print(graph)