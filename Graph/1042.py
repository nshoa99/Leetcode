import collections
# 1. Xây dựng graph
# 2. Tạo 1 dic lưu đỉnh nào trồng hoa gì
# 3. Lặp qua các đỉnh trong graph
# 3.1 Tạo 1 set {1, 2, 3 ,4}
# 3.2 Lặp qua các đỉnh kề của đỉnh đang lặp
# 3.2.1 Tìm ra đỉnh này đang trồng hoa gì dựa vào dic
# 3.2.2 Xóa hoa này ra khỏi set
# 3.3 Đặt phần tử đầu tiên còn lại trong set là hoa sẽ trồng cho đỉnh này 
# 3.4 Return danh sách

def gardenNoAdj(n, paths):
    graph = [[] for _ in range(n + 1)]
    for path in paths:
        u, v = path 
        graph[u].append(v)
        graph[v].append(u)
    
    result = collections.defaultdict(int)

    for u in range(1, n + 1):
        flowers = {1, 2, 3, 4}
        for v in graph[u]:
            if result[v] in flowers:
                flowers.remove(result[v])
        result[u] = list(flowers)[0]

    return result 


print(gardenNoAdj(n = 3, paths = [[1,2],[2,3],[3,1]]))