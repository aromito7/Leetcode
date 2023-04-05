# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, target = None):
    stack = [node.val]
    if node.left:
        left_stack = dfs(node.left, target)
        if left_stack == True:
            return True
    else:
        left_stack = [None]
    if node.right:
        right_stack = dfs(node.right, target)
        if right_stack == True:
            return True
    else:
        right_stack = [None]
    stack += left_stack + right_stack

    return True if target == stack else stack
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        stack1 = [root]
        stack2 = [subRoot]

        return True if dfs(root, dfs(subRoot)) == True else False
        

