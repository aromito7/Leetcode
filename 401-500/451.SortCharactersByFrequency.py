class Solution:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(lambda: 0)

        for l in s:
            dic[l] += 1

        values = sorted([[key, dic[key]] for key in dic], key = lambda v: -v[1])

        output = ''

        for v in values:
            output += v[0] * v[1]


        return output
