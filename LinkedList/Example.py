# Linked List / Danh sách liên kết
# Thêm, xóa phần từ vào mảng thì tốn O(n) -> Với linked list chỉ tốn O(1)
# Sử dụng con trỏ, không sử dụng chỉ mục để truy cập 
# Tốn thêm không gian lưu trữ bộ nhớ cho con trỏ

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "{}-{}".format(self.val, self.next.val)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
    
    def placeOnTop(self, new_val):      # O(1)
        # Tạo ra nốt này
        new_node = Node(new_val)
        # Trỏ node này đến HEAD hiện tại
        new_node.next = self.head
        # Đặt nốt này là head 
        self.head = new_node
    
    def append(self, new_val):
        # Tạo ra nốt này
        new_node = Node(new_val)

        # Nếu Linked List là rỗng, thì set nốt này thành Head
        if not self.head:
            self.head = new_node
            return 
        
        # Nếu Linked List không rỗng, duyệt đến phần tử cuối cùng
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    def insert(self, target_node, new_val):
        if not target_node:
            return 
        
        new_node = Node(new_val)
        new_node.next = target_node.next
        target_node.next = new_node

    def delete(self, target):
        current = self.head
        if current is not None:
            if current.val == target:
                self.head = current.next
                current = None
                return
        
        while current:
            if current.val == target:
                break
            pre = current 
            current = current.next
        
        pre.next = current.next
        current = None




    
linkedList = LinkedList()
Hanoi = Node('Ha Noi')
QuangBinh = Node('Quang Binh')
Danang = Node('Da nang')
Saigon = Node('Sai Gon')

linkedList.head = Hanoi
Hanoi.next = QuangBinh
QuangBinh.next = Danang
Danang.next = Saigon

# linkedList.printList()


### Thêm một phần tử vào Linked List
## Thêm 1 phần từ vào đầu linked list, time complexity O(1

# Tạo ra 1 phần tử mục tiêu
# Trỏ phần từ mục tiêu này đến HEAD hiện tại
# Đặt phần tử mục tiêu này thành HEAD của Linked List

linkedList.placeOnTop('Ha Giang')
#linkedList.printList()

## Thêm 1 phần tử vào cuối Linked list, time complexity O(n)

# Tạo ra 1 phần tử mục tiêu
# Nếu Linked List là rỗng -> set phần tử mục tiêu là head
# Nếu Linked List là không rỗng -> duyệt đến phần tử cuối cùng 
# Trỏ phần tử cuối cùng đến phần tử mục tiêu

linkedList.append('Ca Mau')
linkedList.printList()

## Thêm 1 phần tử vào sau 1 phần tử vào sau 1 phần tử bất kỳ, time complexity O(1) or O(n)

second = linkedList.head.next
linkedList.insert(second, 'Nghe An')
linkedList.printList()


# Xóa 1 phần tử
linkedList.delete('Nghe An')
linkedList.printList()