class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.encode('ascii')
        opens = 0
        jokers = 0

        for letter in s:
            if letter == '(':
                opens += 1
            elif letter == '*':
                jokers += 1
            else:
                if opens > 0:
                    opens -= 1
                elif jokers > 0:
                    jokers -= 1
                else:
                    return False

        opens = 0
        jokers = 0
        for i in range(len(s) - 1, -1, -1):
            letter = s[i]
            if letter == ')':
                opens += 1
            elif letter == '*':
                jokers += 1
            else:
                if opens > 0:
                    opens -= 1
                elif jokers > 0:
                    jokers -= 1
                else:
                    return False


            print(letter, opens, jokers)

        return True if jokers >= opens else False
