# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        nodes = []
        node = head

        while node:
            nodes += [node]
            node = node.next

        length = len(nodes)

        for i in range(length//2):
            nodes[i].next = nodes[length - 1 - i]
        for i in range(length//2 + 1, length):
            nodes[i].next = nodes[length - i]

        nodes[length//2].next = None
            

        return head
