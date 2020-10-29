# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# def reverse(head):
#     tmp, pre = None, None
#     while head:
#         tmp = head.next
#         head.next = pre
#         pre = head
#         head = tmp
#     return pre

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         i, j, k = head, head, head
#         # i: slower, j:faster
#         while j and j.next:
#             i = i.next
#             j = j.next.next

#         i = reverse(i)
        
#         while i:
#             if i.val != k.val:
#                 return False
#             i = i.next
#             k = k.next
#         return True

        
            

            
            
            
        