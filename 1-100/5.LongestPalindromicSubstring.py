class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        s = ''.join([letter.encode('ascii') for letter in s])

        output = s[0]
        
        for i in range(len(s) - 1):
            delta = 1
            while 0 <= i - delta < i + delta < len(s) and s[i - delta] == s[i + delta]:
                if 2 * delta + 1 > len(output):
                    output = s[i - delta: i + delta + 1]
                delta += 1
            
            delta = 0
            if s[i] == s[i + 1]:
                while 0 <= i - delta < i + delta + 1 < len(s) and s[i - delta] == s[i + delta + 1]:
                    if 2 * delta + 2 > len(output):
                        output = s[i - delta: i + delta + 2]
                    delta += 1



        return output
