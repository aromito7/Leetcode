class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        ymin, xmin = 0, 0
        ymax, xmax = len(matrix) - 1, len(matrix[0]) - 1
        ycur, xcur = ymax//2, xmax//2

        if not(matrix[0][0] <= target <= matrix[ymax][xmax]):
            print(False, "first")
            return False


        if target >= matrix[ymax][0]:
            ycur = ymax
        else:
            while not(matrix[ycur][0] < target < matrix[ycur + 1][0]):
                print(ymin, ycur, ymax)
                ycur = (ymin + ymax)//2
                temp = matrix[ycur][0]
                print(target, temp, target > temp, target < temp)
                if target > temp:
                    ymin = ycur
                elif target < temp:
                    ymax = ycur
                else:
                    print(True, "second")
                    return True
        
        if matrix[ycur][xmax] == target:
            return True
        while xmin < xcur < xmax:
            print(xmin, xcur, xmax)
            temp = matrix[ycur][xcur]
            if target > temp:
                xmin = xcur
            elif target < temp:
                xmax = xcur
            else:
                print(True, "third")
                return True
            
            xcur = (xmin + xmax)//2

        if matrix[ycur][xcur] == target:
            return True
        print(False, "last")
        return False
