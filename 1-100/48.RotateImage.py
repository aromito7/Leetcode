class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        l = len(matrix)

        for i in range(l//2):
            for j in range((l + 1)//2):
                matrix[i][j], matrix[l - j - 1][i], matrix[l - i - 1][l - j - 1], matrix[j][l - i - 1] = matrix[l - j - 1][i], matrix[l - i - 1][l - j - 1], matrix[j][l - i - 1], matrix[i][j]
                # print("Interation:")
                # print(matrix[i][j])
                # print(matrix[l - j - 1][i])
                # print(matrix[l - i - 1][l - j - 1])
                # print(matrix[j][l - i - 1])


        return matrix
