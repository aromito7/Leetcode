def combos(groups, remaining):
    if remaining == 0:
        return [[]]
    elif len(groups) == 0 or remaining < 0:
        return []


    group, groups = groups[0], groups[1:]
    output = []

    for i in range(group[1] + 1):
        temp = combos(groups, remaining - i * group[0])
        output += [[group[0]] * i + t for t in temp]

    return output

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates = sorted(candidates)
        cur = candidates[0]
        groups = [[cur, 1]]
        
        for num in candidates[1:]:
            if num == cur:
                groups[-1][1] += 1
            else:
                cur = num
                groups += [[num, 1]]


        return combos(groups, target)
