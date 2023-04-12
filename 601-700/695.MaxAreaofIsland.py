class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = [[0] * (len(grid[0]) + 2)] + [[0] + row + [0] for row in grid] + [[0] * (len(grid[0]) + 2)]
        output = 0
        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[y]) - 1):
                if grid[y][x] == 0: 
                    continue

                count = 0
                stack = [[y,x]]
                while len(stack) > 0:
                    cur = stack.pop()
                    dy, dx = cur[0], cur[1]
                    if grid[dy][dx] == 1:
                        count += 1
                        grid[dy][dx] = 0
                    
                    
                    if grid[dy + 1][dx] == 1:
                        stack += [[dy + 1, dx]]
                    if grid[dy - 1][dx] == 1:
                        stack += [[dy - 1, dx]]
                    if grid[dy][dx + 1] == 1:
                        stack += [[dy, dx + 1]]
                    if grid[dy][dx - 1] == 1:
                        stack += [[dy, dx - 1]]
                output = max(output, count)
                    
            

        return output
