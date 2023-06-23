# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def bfs(root):
    pass

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        maximum = [float("-inf"), 0]
        level = 0
        
        while stack:
            temp = []
            total = 0
            level += 1

            while stack:
                cur = stack.pop()
                total += cur.val

                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            
            if total > maximum[0]:
                maximum = [total, level]
            stack = temp

        return maximum[1]

