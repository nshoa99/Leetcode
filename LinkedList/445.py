# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         stack1, stack2 = [], []
#         while l1:
#             stack1.append(l1.val)
#             l1 = l1.next
        
#         while l2:
#             stack2.append(l2.val)
#             l2 = l2.next
        
#         tmp = []
#         carry = 0 
#         while stack1 and stack2:
#             sum = stack1.pop() + stack2.pop() + carry
#             carry, mod = divmod(sum, 10)
#             tmp.append(mod)
        
#         if len(stack1) > 0:
#             while stack1:
#                 sum = stack1.pop() + carry
#                 carry, mod = divmod(sum, 10)
#                 tmp.append(mod)
#         elif len(stack2) > 0:
#             while stack2:
#                 sum = stack2.pop() + carry
#                 carry, mod = divmod(sum, 10)
#                 tmp.append(mod)
        
#         if carry == 1:
#             tmp.append(carry)
        
#         tmp = tmp[::-1]
#         final = node = ListNode(tmp[0])
#         for i in range(1, len(tmp)):
#             node.next = ListNode(tmp[i])
#             node = node.next
#         return final 
        
            
# # :)

        

        
                
            
        