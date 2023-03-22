import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        s = re.sub(r'[^0-9a-z]+', '', s)
        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start] == s[end]: return False 
            start += 1
            end -= 1

        return True
