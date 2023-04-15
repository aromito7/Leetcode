class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals = sorted(intervals, key = lambda interval: interval[0])

        cur = intervals[0]
        count = 0

        for interval in intervals[1:]:
            if interval[0] < cur[1]:
                count += 1
                if interval[1] < cur[1]:
                    cur = interval
            else:
                cur = interval


        return count
