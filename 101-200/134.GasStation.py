class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        diff = [gas[i] - cost[i] for i in range(length)]

        if sum(diff) < 0:
            return -1
        

        cur = 0
        start = -length

        for i in range(-length, length):
            if i - start == length:
                return start + length
            cur += diff[i]
            while cur < 0:
                cur -= diff[start]
                start += 1

        return -1
