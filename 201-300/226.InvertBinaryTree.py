# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        stack = [root]

        while len(stack) > 0:
            cur = stack.pop()
        
            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                stack += [cur.left]
            if cur.right:
                stack += [cur.right]

        return root

