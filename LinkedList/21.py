  
# ### DO NOT REMOVE THIS
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ### DO NOT REMOVE THIS

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         result = current = ListNode()
                
#         while l1 and l2:
#             if l1.val > l2.val:
#                 current.next = l2
#                 l2 = l2.next
#             else:
#                 current.next = l1
#                 l1 = l1.next
                
#             current = current.next
        
#         current.next = l1 or l2
#         return result.next