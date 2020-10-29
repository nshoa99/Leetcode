# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         lengthA, lengthB = 0, 0 
#         tmpA, tmpB = headA, headB
        
#         while tmpA:
#             lengthA +=1
#             tmpA = tmpA.next
        
#         while tmpB:
#             lengthB += 1
#             tmpB = tmpB.next
        
#         if lengthA > lengthB:
#             for i in range(lengthA - lengthB):
#                 headA = headA.next
#         else:
#             for i in range(lengthB - lengthA):
#                 headB = headB.next
        
#         while headA != headB:
#             headA = headA.next
#             headB = headB.next
#         return headA
        
            
        