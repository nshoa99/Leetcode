# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val = 0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        len = 0
        result = []
        tmp = root
        
        # Tính chiều dài của root
        while tmp:
            len += 1
            tmp = tmp.next
        
        # Nếu k >= chiều dài -> chia ra làm k phần, mỗi phần 1 phần tử
        if k >= len:
            for i in range(k):            
                if i < len:
                    node = ListNode()
                    node.val = root.val
                    result.append(node)
                    root = root.next
                else:
                    result.append(None)
        
        # Nếu k < chiều dài -> tính số phần tử của mỗi phần
        else:
            x, y = divmod(len, k)
            numOfEle = [x] * k
            
            # Vòng lặp while để đảm bảo số phần tử của các phần đầu tiên luôn lớn hơn hoặc bằng các phần ở sau. 
            i = 0
            while y > 0:
                numOfEle[i] += 1
                y -= 1
                i += 1
            
            for num in numOfEle:
                for i in range(num):
                    if i == 0:
                        result.append(root)
                        
                    if i == num - 1:
                        tmp = root.next
                        root.next = None
                        root = tmp
                    else:
                        root = root.next
                                
        return result
                
        