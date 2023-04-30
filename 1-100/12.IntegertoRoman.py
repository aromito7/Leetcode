class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']]

        output = ''


        for power in range(3, -1, -1):
            cur = num // (10 ** power)
            num %= 10 ** power

            if cur == 1:
                output += symbols[power][0]
            elif cur == 2:
                output += symbols[power][0] + symbols[power][0]
            elif cur == 3:
                output += symbols[power][0] + symbols[power][0] + symbols[power][0]
            elif cur == 4:
                output += symbols[power][0] + symbols[power][1]
            elif cur == 5:
                output += symbols[power][1]
            elif cur == 6:
                output += symbols[power][1] + symbols[power][0]
            elif cur == 7:
                output += symbols[power][1] + symbols[power][0] + symbols[power][0]
            elif cur == 8:
                output += symbols[power][1] + symbols[power][0] + symbols[power][0] + symbols[power][0]
            elif cur == 9:
                output += symbols[power][0] + symbols[power + 1][0]

            print(num, cur, power, output)

        return output
