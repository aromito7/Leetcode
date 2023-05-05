class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split(' ')

        while not words[-1]:
            words.pop()

        return len(words[-1])
