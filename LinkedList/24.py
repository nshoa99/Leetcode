# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         length = 0
#         aList = []
#         tmp = head
        
#         while tmp:
#             length += 1
#             aList.append(tmp.val)
#             tmp = tmp.next
        
#         if length == 0 or length == 1:
#             return head
        
#         i = 0
#         while i < length - 1:
#             aList[i], aList[i + 1] = aList[i + 1], aList[i]
#             i += 2
        
#         final = node = ListNode(aList[0])
#         for i in range(1, length):
#             node.next = ListNode(aList[i])
#             node = node.next
        
#         return final 


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = node = ListNode(0)
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            node.next = tmp
            head = head.next
            node = tmp.next
        return dummy.next
            
            

            

        
        
       
    
        