class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = 0
        width = 0

        output = 0

        dic = {}

        while start + width < len(s):
            char = s[start + width]
            window = s[start: start + width]
            if char in s[start: start + width]:
                while char in s[start: start + width]:
                    start += 1
                    width -= 1
            else:
                width += 1
                if width > output:
                    output = width
                

        return output
        
