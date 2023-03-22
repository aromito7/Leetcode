class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dic = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for letter in s:
            if letter in ['(', '{', '[']:
                stack += [letter]
            elif letter in [')', '}', ']']:
                if len(stack) == 0 or stack.pop() != dic[letter]:
                    return False
        

        return len(stack) == 0
