class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vows = []
        s = list(s)

        for i, letter in enumerate(s):
            if letter in vowels:
                vows.append(i)


        for i in range(len(vows)//2):
            s[vows[i]], s[vows[-1 - i]] = s[vows[-1 - i]], s[vows[i]]

        return ''.join(s)
