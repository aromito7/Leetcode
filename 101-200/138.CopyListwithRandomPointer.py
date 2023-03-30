"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
def printNodes(head):
    output = []
    cur = head
    while cur:
        nex = cur.next.val if cur.next else None
        ran = cur.random.val if cur.random else None
        output += [[nex, ran]]
        cur = cur.next
    print(output)
    return output

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        cur = head
        rands = []
        vals = []

        while cur:
            cur.id = len(vals)
            vals += [cur.val]
            cur = cur.next

        cur = head
        while cur:
            rands += [cur.random.id] if cur.random else [None]
            cur = cur.next



        copy = [Node(val) for val in vals]
        copy += [None]
        vals += [None]
        for i, node in enumerate(copy[:-1]):
            node.next = copy[i + 1]
            node.random = copy[rands[i]] if rands[i] is not None else None


        return copy[0]
    

