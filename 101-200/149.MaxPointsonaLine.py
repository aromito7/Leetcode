class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        output = 0
        dic = defaultdict(lambda: 0)

        for i, p1 in enumerate(points):
            for j in range(i + 1, len(points)):
                x1, y1 = p1
                x2, y2 = points[j]
                print(x1, y1, x2, y2)

        return output
