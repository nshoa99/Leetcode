# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         lenth = 0
#         tmp = head
#         while tmp:
#             tmp = tmp.next
#             lenth += 1
        
#         middle = lenth // 2
        
#         i = 0
#         current = head
#         while i < middle:
#             current = current.next
#             i += 1
#         return current
            
            
# Time complexity O(n), Extra space complexity O(1)


# # Cach 2
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         i, j = head, head
#         while i and i.next:
#             i = i.next.next
#             j = j.next
#         return j 

# Time complexity O(n), Extra space complexity O(1)


            
        
        
