import queue

matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 0, 0]
]

s = (4, 1) # (x, y)

# 1. Tạo mảng visited có chiều chính bằng ma trận
# 2. Đánh dấu s là đã thăm, visited[x][y] = True
# 3. Bỏ vào queue: q.put(s)
# 4. Tạo vòng lặp while với điều kiện là q không rỗng
# 4.1 Lấy phần tử đầu tiên khỏi q: q = q.get()
# 4.2 Tìm ra tọa độ của 4 điểm xung quanh. Lặp qua các tọa độ này
# 4.2.1. Nếu tọa độ này thỏa mãn 3 đk: a. Không nằm ngoài mảng b. Giá trị của tại tọa độ này = 1 c. Nó chua thăm
# 4.2.1.1 Đánh dấu là đã thăm 
# 4.2.1.2 Thêm vào trong q


import queue
q = queue.Queue()

m = len(matrix)
n = len(matrix[0])
visited = [
    [False for i in range(n)] for _ in range(m)
]
visited[s[0]][s[1]] = True
q.put(s)

def isOK(x, y, m, n):
    return x >= 0 and x < m and y >= 0 and y < n

cnt = 0
while not q.empty():
    u = q.get()
    cnt +=1
    x, y = u
    xRows = [0, 0, -1, 1]
    yCols = [-1, 1, 0, 0]
    for i in range(4):
        new_x = x + xRows[i]
        new_y = y + yCols[i]
        if isOK(new_x, new_y, m, n) and matrix[new_x][new_y] == 1 and not visited[new_x][new_y]:
            q.put((new_x, new_y))
            visited[new_x][new_y] == True


