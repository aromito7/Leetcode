# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        

        if not root:
            return 0
        
        stack = [[root, 1]]
        output = 1

        while len(stack) > 0:
            cur, depth = stack.pop()
            if depth > output:
                output = depth
            if cur.right:
                stack += [[cur.right, depth + 1]]
            if cur.left:
                stack += [[cur.left, depth + 1]]

        return output
