class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        s = s.encode('ascii')

        letters = defaultdict(lambda: [-1, -1])

        for i, l in enumerate(s):
            if letters[l][0] == -1:
                letters[l][0] = i
            letters[l][1] = i

        end = -1
        output = []
        ranges = sorted(letters.values(), key = lambda r: r[0])

        for r in ranges:
            if r[0] > end:
                #print(r, end)
                output += [r[0]]
                end = r[1]
            elif r[0] < end < r[1]:
                end = r[1]
        
        output += [len(s)]

        

        return [output[i+1] - output[i] for i in range(len(output) - 1)]
