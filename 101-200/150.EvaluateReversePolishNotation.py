class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        i = 0
        while tokens[i] not in ['+', '-', '*', '/']:
            stack += [int(tokens[i])]
            i += 1

        while i < len(tokens):
            if tokens[i] == '+':
                stack = stack[:-2] + [stack[-2] + stack[-1]]
            elif tokens[i] == '-':
                stack = stack[:-2] + [stack[-2] - stack[-1]]
            elif tokens[i] == '*':
                stack = stack[:-2] + [stack[-2] * stack[-1]]
            elif tokens[i] == '/':
                result = stack[-2] / stack[-1]
                if not stack[-2] % stack[-1] == 0:
                    if result >= 0:
                        result = int(result)
                    else:
                        result = int(result) + 1
                stack = stack[:-2] + [result]
            else:
                stack += [int(tokens[i])]
            i += 1
        
        return stack[0]
