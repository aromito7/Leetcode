# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def search(self, node):
        if node.left:
            left, left_diameter = self.search(node.left)
        else:
            left, left_diameter = 0, 0
        if node.right:
            right, right_diameter = self.search(node.right)
        else:
            right, right_diameter = 0, 0

        depth = max(left, right) + 1
        diameter = max(left_diameter, right_diameter, left + right)

        return depth, diameter

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth, diameter = self.search(root)



        return diameter
