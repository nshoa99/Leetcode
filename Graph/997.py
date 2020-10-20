import collections
def findJugde(N, trust):
    # Tạo ra đồ thị A đại diện cho mình tin người khác
    # Tạo đồ thị B đại diện cho người khác tin mình 
    graphA = collections.defaultdict(list)                  # O(v)
    graphB = collections.defaultdict(list)                  # O(v)

    for item in trust:                                      # O(e)
        graphA[item[0]].append(item[1])                     
        graphB[item[1]].append(item[0])                     
    
    for i in range(1, N + 1):                               # O(e)
        if len(graphA[i]) == 0 and len(graphB[i]) == N - 1:
            return i
    return -1

print(findJugde(N = 3, trust = [[1,3],[2,3]]))            

    # Lặp qua các chỉ mục, ở 1 vị trí nào đó mà:
    # if len(A[i]) == 0 and len(B[i]) == N - 1 

# Time complexity O(max(v, e)), extra space complexity O(v)
