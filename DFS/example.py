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

visited = [False for _ in range(V)]
path = [-1 for _ in range(V)]
def dfs(start):
    visited[start] = True
    s = []
    s.append(start)

    while s:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u 
                s.append(v)
    
    
dfs(0)
print(path)



# Sử dụng đệ quy

visited = [False for _ in range(V)]
path = [-1 for _ in range(V)]

def dfsRec(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            path[v] = s
            dfs(v)

dfsRec(0)
print(path)
    
