class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda interval: interval[0])
        output = intervals[:1]

        for interval in intervals[1:]:
            if interval[0] <= output[-1][1]:
                output[-1][1] = max(interval[1], output[-1][1])
                #output[-1][0] = min(interval[0], output[-1][0])
            else:
                output += [interval]

        return output
