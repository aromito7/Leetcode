# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        output = []

        cur_level = [root]

        while len(cur_level) > 0:
            next_level = []
            output += [cur_level[-1].val]

            for node in cur_level:
                if node.left:
                    next_level += [node.left]
                if node.right:
                    next_level += [node.right]
            
            cur_level = next_level

        return output
