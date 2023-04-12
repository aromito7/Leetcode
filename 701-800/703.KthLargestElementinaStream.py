class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = sorted(nums)[-k:]
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        i = 0
        start = 0
        end = len(self.nums) - 1
        i = (start + end)//2
        while start < end:
            if val > self.nums[i]:
                start = i
                i = (start + end + 1)//2
            elif val < self.nums[i]:
                end = i
                i = (start + end)//2
            else:
                break

        self.nums = (self.nums[:i] + [val] + self.nums[i:])[-self.k:]

        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
