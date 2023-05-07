# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        nodes = set()
        nodes.add(head.val)

        # if not head:
        #     return head
        cur = head

        while cur.next:
            if cur.next.val not in nodes:
                nodes.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next


        return head
