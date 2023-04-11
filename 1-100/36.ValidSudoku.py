class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val == '.':
                    continue
                
                if val in rows[y] or val in cols[x] or val in squares[(y//3, x//3)]:
                    return False

                rows[y].add(val)
                cols[x].add(val)
                squares[(y//3, x//3)].add(val)


        return True
