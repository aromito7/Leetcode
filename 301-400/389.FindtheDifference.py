class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = defaultdict(lambda: 0)

        for letter in s:
            dic[letter] += 1

        for letter in t:
            dic[letter] -= 1
            if dic[letter] < 0:
                return letter
