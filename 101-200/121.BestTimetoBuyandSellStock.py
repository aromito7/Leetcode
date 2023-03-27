class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        lowest = 0
        current = 1
        profit = 0

        while current < len(prices):
            low = prices[lowest]
            cur = prices[current]
            if cur - low > profit:
                profit = cur - low
            if cur < low:
                lowest = current
            current += 1

        return profit

