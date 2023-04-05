# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search(node, k):
    results = []
    if node.left:
        results += search(node.left, k)
    results += [node.val]

    if len(results) > k:
        return results

    if node.right:
        results += search(node.right, k)
    
    return results

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        return search(root, k)[k - 1]
