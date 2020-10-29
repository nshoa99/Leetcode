# class Solution:
#     def __init__(self, hasCycle, isOk):
#         self.hasCycle = hasCycle
#         self.isOk = isOk
    
#     def leadsToDestination(n, edges, source, destination):
#         graph = [[] for _ in range(n)]
#         for edge in edges:
#             u, v = edge
#             graph[u].append(v)
        
#         self.hasCycle = False
#         self.isOk = True
#         visited = [0 for _ in range(n)]

#         def dfs(s):
#             if not len(graph[s]) and s != destination:
#                 self.isOk = False

#             for v in graph[s]:
#                 if visited[v] == 0:
#                     visited[v] = 1
#                     dfs(v)
#                 elif visited[v] == 1:
#                     self.hasCycle = True
                
#                 visited[v] = 2
#         visited[source] = True
#         dfs(source)

#         return self.isOK and not self.hasCycle


    