class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]

        for y in range(1, len(grid)):
            for x in range(1, len(grid[y])):
                grid[y][x] += min(grid[y-1][x], grid[y][x-1])

        return grid[-1][-1]
