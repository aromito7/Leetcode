class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        while word1 and word2:
            output += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]

        output += word1 + word2

        return output
