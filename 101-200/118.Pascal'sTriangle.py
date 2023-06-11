class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(1, numRows):
            cur = [1, 1]
            for num in output[-1][1:]:
                cur[-1] += num
                cur.append(num)
            output.append(cur)


        return output



