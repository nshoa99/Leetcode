# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next


# class Solution(object):
#     def reverseBetween(self, head, m, n):
        
#         result = ListNode(0)
#         result.next = head
        
#         current, prev = head, result
        
#         for i in range(m - 1):
#             current = current.next
#             prev = prev.next
        
#         print(current)
#         print(prev)
        
#         for i in range(n - m):
#             tmp = current.next
#             current.next = tmp.next
#             tmp.next = prev.next
#             prev.next = tmp

#         return result.next
        
            
        