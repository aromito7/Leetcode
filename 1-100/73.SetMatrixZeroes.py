class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ry = range(len(matrix))
        rx = range(len(matrix[0]))
        y0 = set()
        x0 = set()

        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val == 0:
                    if y in ry: 
                        ry.remove(y)
                        y0.add(y)
                    if x in rx:
                        rx.remove(x)
                        x0.add(x)

        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if y in y0 or x in x0:
                    matrix[y][x] = 0

        return matrix
