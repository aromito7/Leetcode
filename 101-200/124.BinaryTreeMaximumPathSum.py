# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def recurse(self, node):
        left_path = [0, float('-inf')]
        right_path = [0, float('-inf')]
        if node.left:
            left_path = self.recurse(node.left)

        if node.right:
            right_path = self.recurse(node.right)




        longest_path = max(left_path[0], right_path[0], 0) + node.val
        chain = max(left_path[0], 0) + max(right_path[0], 0) + node.val

        longest_chain = max(left_path[1], right_path[1], chain)
        return [longest_path, longest_chain]


    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        #stack = [root]
        maximum = 0

        maximum = self.recurse(root)

        # while len(stack) > 0:
        #     curr = stack.pop()

        #     if curr.right: 
        #         stack += [curr.right]
        #     if curr.left:
        #         stack += [curr.left]


        return maximum[1]
