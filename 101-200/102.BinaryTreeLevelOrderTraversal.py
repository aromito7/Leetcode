# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = [root]
        cur = root
        output = []
        cur_level = [root]

        while len(cur_level) > 0:
            level_output = []
            next_level = []
            for node in cur_level:
                level_output += [node.val]
                if node.left:
                    next_level += [node.left]
                if node.right:
                    next_level += [node.right]
            output += [level_output]
            cur_level = next_level


        return output
