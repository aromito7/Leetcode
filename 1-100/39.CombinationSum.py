def combos(candidates, target):
    if len(candidates) == 1:
        if target % candidates[0] == 0:
            return [[candidates[0]] * (target//candidates[0])]
        
        return []

    cur, candidates = candidates[-1], candidates[:-1]
    output = []
    for i in range(1 + target//cur):
        temp = [combo for combo in combos(candidates, target) if combo != False]
        output += [t + [cur] * i for t in temp]

        target -= cur
    
    return output

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        return(combos(candidates, target))
