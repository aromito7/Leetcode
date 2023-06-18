class RecentCounter:

    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:
        stack = self.stack
        
        i = 0

        while i < len(stack) and t - stack[i] > 3000:

            i += 1

        stack = stack[i:]
        self.stack = stack
        stack.append(t)

        return len(stack)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
