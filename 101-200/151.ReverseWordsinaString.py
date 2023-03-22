class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([word for word in s.split(' ') if len(word) > 0][::-1])
