class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ranges = []

        chains = {}
        max_length = 0
        for num in nums:
            if num in chains: continue
            if (num - 1) in chains and (num + 1) in chains:
                chains[num - 1].append(num)
                chains[num] = chains[num - 1]
                n = num + 1
                while n in chains:
                    chains[num].append(n)
                    chains[n] = chains[num]
                    n += 1
            elif (num - 1) in chains:
                chains[num - 1].append(num)
                chains[num] = chains[num - 1]
            elif (num + 1) in chains:
                chains[num + 1].append(num)
                chains[num] = chains[num + 1]
            else:
                new_chain = [num]
                chains[num] = new_chain
            
            if len(chains[num]) > max_length:
                max_length = len(chains[num])


        return max_length
