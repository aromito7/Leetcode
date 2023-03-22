class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = [float('inf')]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack += [val]
        if val <= self.min[-1]:
            self.min += [val]

    def pop(self):
        """
        :rtype: None
        """

        output = self.stack[-1]
        self.stack = self.stack[:-1]
        if output == self.min[-1]:
            self.min.pop()
        return output
        

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
