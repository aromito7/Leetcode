class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = prices[0]
        sell = None
        output = 0

        for p in prices[1:]:
            if sell:
                if p + fee < sell:
                    output += sell - buy - fee
                    buy = p
                    sell = None
                elif p > sell:
                    sell = p
            elif buy + fee < p:
                sell = p

            if p < buy:
                buy = p

        if sell and buy + fee < sell:
            output += sell - buy - fee


        return output
