edges = [[0,1],[1,2],[2,3],[3,4],[4,0]]
n = 5

graph = [[] for _ in range(n)]

for edge in edges:
    u, v = edge
    graph[u].append(v)

check = {'hasACycle': False}
visited =[0 for _ in range(n)] 

def dfs(s):
    for v in graph[s]:
        if visited[v] == 0:
            visited[v] = 1
            dfs(v)
        elif visited[v] == 1:
            check['hasACycle'] = True
        visited[v] = 2

dfs(0)
print(check)