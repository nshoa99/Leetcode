import queue
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

# V: đỉnh
V = 7
graph = [[] for _ in range(V)]

for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*V
path = [-1]*V
 
# Queue -> FIFO, lấy phần tử đầu tiên của mảng
q = queue.Queue()

# Set điểm xuất phát là đã thăm 
s = 0               # Xuất phát từ điểm 0 
visited[s] = True

# Thêm vào queue
q.put(s)

# Chạy hàm while với điều kiện là Q không rỗng
while not q.empty():
    u = q.get()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            path[v] = u
            q.put(v)

# Time complexity O(V + E)

def shortestPath(e):
    aList = []
    while path[e] != -1:
        aList.append(e)
        e = path[e]
    aList.append(e)
    return aList

print(shortestPath(3))