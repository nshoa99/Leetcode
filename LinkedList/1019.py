# Cách 1, chyển Linked List về List rồi tính toán

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def nextLargerNodes(self, head: ListNode) -> List[int]:
#         aList = []
#         while head:
#             aList.append(head.val)
#             head = head.next
        
#         n = len(aList)
#         result = [0] * n
#         stack = []
#         i = 0
        
#         while i < n:
#             if len(stack) == 0 or aList[i] <= stack[-1][0]:
#                 stack.append([aList[i], i])
#                 i += 1
#             else:
                
#                 result[stack[-1][1]] = aList[i]
#                 stack.pop()
        
#         return result