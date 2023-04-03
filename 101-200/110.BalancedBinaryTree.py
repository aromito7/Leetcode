# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_balanced(node):
    if node.left:
        left = is_balanced(node.left)
    else:
        left = 0

    if node.right:
        right = is_balanced(node.right)
    else:
        right = 0

    if left == -1 or right == -1:
        return -1
    if (left - right) ** 2 > 1:
        return -1

    return max(left, right) + 1

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        return True if is_balanced(root) > 0 else False
