# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        length = 0

        while cur:
            length += 1
            cur = cur.next

        length = (length // 2 ) - 1

        if length < 0:
            return None

        cur = head
        while length > 0:
            length -= 1
            cur = cur.next

        
        cur.next = cur.next.next

        return head
        

