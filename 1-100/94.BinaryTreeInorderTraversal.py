# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recurse(node):
    output = []
    if node.left:
        output += recurse(node.left)
    
    output += [node.val]

    if node.right:
        output += recurse(node.right)

    return output

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        return recurse(root)
