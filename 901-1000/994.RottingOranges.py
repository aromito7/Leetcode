class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        remaining = 0
        rotten = []
        time = 1
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 2:
                    rotten += [(y, x)]
                elif val == 1:
                    remaining += 1
        
        if remaining == 0:
            return 0

        #print(remaining, rotten, grid)

        
        while len(rotten) > 0:
            next_stack = []

            while len(rotten) > 0:
                y, x = rotten.pop()
                #print(y, x)
                for dy, dx in delta:
                    if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]) and grid[y + dy][x + dx] == 1:
                        # print("Turned Rotten:")
                        # print(y + dy, x + dx)
                        grid[y + dy][x + dx] = 2
                        next_stack += [(y + dy, x + dx)]
                        remaining -= 1
                        if remaining == 0:
                            return time
            
            rotten = next_stack
            time += 1


        return -1
