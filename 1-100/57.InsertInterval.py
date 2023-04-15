class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        beginning = []
        middle = [newInterval[0], newInterval[1]]
        end = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                beginning += [interval]
            elif interval[0] > newInterval[1]:
                end += [interval]
            else:
                middle[0] = min(middle[0], interval[0])
                middle[1] = max(middle[1], interval[1])

            


        return beginning + [middle] + end
