class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = [1]

    def popSmallest(self) -> int:
        smallest = self.smallest

        if len(smallest) == 1:
            smallest[0] += 1
            return smallest[0] - 1
        else:
            output, self.smallest = smallest[0], smallest[1:]
            return output

    def addBack(self, num: int) -> None:
        smallest = self.smallest
        if num < smallest[-1] and num not in smallest:
            smallest.append(num)
            self.smallest = sorted(smallest)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
