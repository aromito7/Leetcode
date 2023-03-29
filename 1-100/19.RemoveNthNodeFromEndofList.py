# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        cur = head
        length = 0

        while cur:
            cur = cur.next
            length += 1
            
        cur = head
        if n <= length - 1:
            if n == 0:
                return head.next
            for i in range(length - n - 1):
                cur = cur.next
            cur.next = cur.next.next
        if n == length:
            return head.next
                

        return head
        
