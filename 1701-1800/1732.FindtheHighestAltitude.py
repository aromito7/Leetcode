class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        ls = []
        ls.append(0)

        for num in gain:
            ls.append(ls[-1] + num)

        return max(ls)
