import collections
edges = [
    [0, 1],
    [0, 2],
    [2, 1],
    [1, 4],
    [4, 2],
    [2, 3],
    [3, 0],
    [5, 6],
    [6, 7]
]
V = 8 # số đỉnh 
E = 9 # số cạnh

# Cách 1: Sử dụng mảng răng cưa

graph = [[] for _ in range(V)] # O(V)

for edge in edges:             # O(E)
    u, v = edge   # u, v = edge[0], edge[1]
    graph[u].append(v)
    
# Time complexity O(V) + O(E) = O(max(E, V))

print(graph)



# Cách 2: Sử dụng dictionary
edges = [
    ["Hà Nội", "Hải Phòng"],
    ["Hà Nội", "Hải Dương"],
    ["Hải Dương", "Quảng Ngãi"],
    ["Hải Dương", "Quảng Bình"],
]

graph = collections.defaultdict(list)

for edge in edges:
    u, v = edge
    graph[u].append(v)

print(graph)