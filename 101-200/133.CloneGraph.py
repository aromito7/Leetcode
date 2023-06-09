"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        q = deque([node])
        clones = {node.val: Node(node.val, [])}

        while q:
            cur = q.popleft()
            clone = clones[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]
