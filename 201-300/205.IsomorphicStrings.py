def translate(s):
        dic = {}
        translation = ''
        count = 0

        for letter in s:
            if letter not in dic:
                count += 1
                dic[letter] = count
            translation += str(dic[letter])

        return translation

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return translate(s) == translate(t)
