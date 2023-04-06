def subsets(groups):
    if len(groups) == 0:
        return [[]]

    group, groups = groups[0], groups[1:]
    output = []
    subs = subsets(groups)
    output = [[group[0]] * i + s for s in subs for i in range(group[1] + 1)]
    return output
        

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        cur = nums[0]
        groups = [[cur, 1]]

        for num in nums[1:]:
            if num == cur:
                groups[-1][1] += 1
            else:
                cur = num
                groups += [[cur, 1]]

        return subsets(groups)
