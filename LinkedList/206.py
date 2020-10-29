# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#         aList = []
#         while head:
#             aList.append(head.val)
#             head = head.next
        
#         aList = aList[::-1]
#         final = node = ListNode(aList[0])
#         for i in range(1, len(aList)):
#             node.next = ListNode(aList[i])
#             node = node.next
        
#         return final 


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         tmp, pre = None, None
#         while head:
#             tmp = head.next
#             head.next = pre
#             pre = head
#             head = tmp 
#         return pre

            
        
        