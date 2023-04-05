# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if q.val < p.val:
            p, q = q.val, p.val
        else:
            p, q = p.val, q.val
        
        while not(p < root.val < q):
            if root.val > q:
                root = root.left
            elif root.val < p:
                root = root.right
            else:
                return root

        return root
