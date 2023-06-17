def add_asteroid(stack, a):
    if a < 0:
        while stack and stack[-1] > 0:
            if stack[-1] + a < 0:
                stack.pop()
            elif stack[-1] + a == 0:
                stack.pop()
                return
            else:
                return

    stack.append(a)
    return

    

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            add_asteroid(stack, a)

        return stack
