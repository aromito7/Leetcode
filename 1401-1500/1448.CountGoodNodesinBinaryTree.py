# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search(node, max_path):
    good_nodes = 0

    if node.val >= max_path:
        good_nodes += 1
        max_path = node.val




    if node.left:
        good_nodes += search(node.left, max_path)
    if node.right:
        good_nodes += search(node.right, max_path)

    return good_nodes

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return search(root, float('-inf'))
