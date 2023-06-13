def valid_rows(row_1, row_2):
    for n in range(len(row_1) - 1):
        if row_1[n] + row_2[n] > 1:
            return False

    return True
            

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        unique_vals = set()
        unique_rows = []

        for i, row in enumerate(grid):
            val = 0
            for num in row:
                val *= 2
                val += num
                

            if val not in unique_vals:
                unique_vals.add(val)
                unique_rows.append(row + [i])
            
        for row in unique_rows:
            if sum(row[:-1]) == 0:
                return [row[-1]]

        for i, row_1 in enumerate(unique_rows):
            for row_2 in unique_rows[i + 1:]:
                if valid_rows(row_1, row_2):
                    return [row_1[-1], row_2[-1]]
        
        return []
