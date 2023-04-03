class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        h = len(matrix)
        w = len(matrix[0])
        

        iterations = 2 * min(h, w) - (1 if h <= w else 0)

        x, y = -1, 0
        output = []
        for i in range(iterations):
            delta = 1 if i % 4 < 2 else -1
            dx = (i + 1) % 2
            dy = i % 2

            iteration = (h if i % 2 else w)
            for j in range(iteration):
                x += delta * dx
                y += delta * dy

                output += [matrix[y][x]]
            
            if i % 2:
                w -= 1
            else:
                h -= 1





        return output


