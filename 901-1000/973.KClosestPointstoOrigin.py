class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        return sorted(points, key = lambda p: p[0] ** 2 + p[1] ** 2)[:k]
