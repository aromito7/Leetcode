class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        output = 1
        
        for i in range(len(s) - 1):
            delta = 1
            output += 1
            while 0 <= i - delta < i + delta < len(s) and s[i - delta] == s[i + delta]:
                delta += 1
                output += 1
            
            delta = 0
            if s[i] == s[i + 1]:
                while 0 <= i - delta < i + delta + 1 < len(s) and s[i - delta] == s[i + delta + 1]:
                    delta += 1
                    output += 1



        return output
