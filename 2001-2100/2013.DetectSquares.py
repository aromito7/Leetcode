class DetectSquares(object):

    def __init__(self):
        self.x_points = defaultdict(lambda: defaultdict(lambda: 0))

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.x_points[x][y] += 1
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """

        x, y = point
        output = 0

        for key in self.x_points[x]:
            length = abs(y - key)
            if length > 0:
                output += self.x_points[x][key] * self.x_points[x - length][key] * self.x_points[x - length][y]
                output += self.x_points[x][key] * self.x_points[x + length][key] * self.x_points[x + length][y]

        return output
        
