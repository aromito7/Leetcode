# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search(node):

    if not node:
        return None
    val = node.val
    if node.left:
        left_temp = search(node.left)
        if left_temp == False or left_temp[1] >= val:
            return False
    else:
        left_temp = None

    if node.right:
        right_temp = search(node.right)
        if right_temp == False or right_temp[0] <= val:
            return False
    else:
        right_temp = None


    return left_temp[0] if left_temp else val, right_temp[1] if right_temp else val

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return False if search(root) == False else True
