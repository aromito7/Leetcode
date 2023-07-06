class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) == 0:
            return []
        output = []

        cur = [None, -1]

        for i, l in enumerate(s):
            if not l == cur[0]:
                if i - cur[1] >= 3:
                    output.append([cur[1], i - 1])
                cur = [l, i]
            
        if i - cur[1] >= 2:
                    output.append([cur[1], i])


        return output
