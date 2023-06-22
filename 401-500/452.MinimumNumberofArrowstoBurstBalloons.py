class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        output = 0
        
        points = sorted(points, key = lambda x: x[0])
        start = float('-inf')
        end = float('-inf')

        for point in points:
            if point[0] > end:
                output += 1
                start = point[0]
                end = point[1]
            else:
                end = min(end, point[1])

        return output
