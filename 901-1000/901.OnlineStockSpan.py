class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        count = 1
        prices = self.prices

        while prices and prices[-1][0] <= price:
            count += prices[-1][1]
            prices.pop()

        prices.append([price, count])

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
