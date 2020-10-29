# Convert Binary Tree to Min Heap 
# Step 1: Tìm điểm bắt đầu lặp
#   start = len(tree) // 2 - 1
# Step 2: Lặp từ điểm start về 0



# Heapify

aTree = [10, 7, 6, 1, 4, 3, 9, 0, 15]

def heapify(aTree, n, i):
    smallest = i
    left_i = 2 * i + 1
    right_i = 2 * i + 2

    if left_i < n and aTree[smallest] > aTree[left_i]:
        smallest = left_i
    if right_i < n and aTree[smallest] > aTree[right_i]:
        smallest = right_i
    if smallest != i:
        aTree[i], aTree[smallest] = aTree[smallest], aTree[i]
        heapify(aTree, n, smallest)


def buildHeap(aTree):
    n = len(aTree)
    start = n // 2 - 1

    # Lặp từ start -> 0
    for i in range(start, -1, -1):
        heapify(aTree, n, i)

buildHeap(aTree)
print(aTree)
# Time complexity O(n)


# min value
print(aTree[0])
# Time complexity O(1)

### Add a new value to a heap 

def insert(val, aTree):
    aTree.append(val)
    i = len(aTree) - 1

    while i >= 1 and aTree[i] < aTree[(i - 1) // 2]:
        aTree[i], aTree[(i-1) // 2] = aTree[(i-1) // 2], aTree[i]
        i = (i-1) // 2

insert(-2, aTree)
print(aTree)

# Time complexity: O(n). Do cây nhị phân đầy đủ


# Delete a value in a Tree

def remove(idx, aTree):
    n = len(aTree)
    aTree[idx] = aTree[-1]
    heapify(aTree, n, 0)
    aTree.pop()

remove(0, aTree)
print(aTree)


aTree = [10, 7, 6, 1, 4, 3, 9, 0, 15]

import queue
hq = queue.PriorityQueue()

for num in aTree:
    # Thêm 1 phần tử vào heap
    hq.put(num)
print("hq = {}".format(hq.queue))

# xóa phần tử đầu tiên khỏi heap
top = hq.get()
print(top)

# Kiểm tra độ dài hiện tại
print(hq.qsize())

# Kiểm tra có rỗng hay không
print(hq.empty())



# Max Heap
class maxHeapItem:
    def __init__(self, val):
        self.val = val
    # overide
    def __lt__(self, other):
        return self.val > other.val

maxHeap = queue.PriorityQueue()
for num in aTree:
    maxHeap.put(maxHeapItem(num))

print(maxHeap.queue[0].val)


import heapq
heapq.heapify(aTree)
print(aTree)

heapq.heappush(aTree, -10)
print(aTree)

heapq.heappop(aTree)
print(aTree)
