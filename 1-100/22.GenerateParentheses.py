class Solution(object):
    def generateNext(self, current, remaining):
        print(current, remaining)
        if remaining[1] == 0:
            return current
        
        if remaining[1] > remaining[0] and remaining[0] > 0:
            temp1 = [c + '(' for c in current]
            temp2 = [c + ')' for c in current]
            output = self.generateNext(temp1, [remaining[0] - 1, remaining[1]]) + self.generateNext(temp2, [remaining[0], remaining[1] - 1])
            return output
        elif remaining[0] == 0:
            temp = [c + ')' for c in current]
            return self.generateNext(temp, [remaining[0], remaining[1] - 1])
        else:
            temp = [c + '(' for c in current]
            return self.generateNext(temp, [remaining[0] - 1, remaining[1]])

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        
        output = ['(']

        output = self.generateNext(output, [n - 1, n])
        
        return output
