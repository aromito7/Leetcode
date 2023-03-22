# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        stack = [[p, q]]
        if p and q:
            if p.val != q.val: 
                return False
            while len(stack) > 0:
                np, nq = stack.pop()

                if np.left and nq.left:
                    if np.left.val != nq.left.val:
                        return False
                    stack += [[np.left, nq.left]]
                elif np.left or nq.left:
                    return False

                if np.right and nq.right:
                    if np.right.val != nq.right.val:
                        return False
                    stack += [[np.right, nq.right]]
                elif np.right or nq.right:
                    return False
        elif p or q:
            return False

        
        return True

