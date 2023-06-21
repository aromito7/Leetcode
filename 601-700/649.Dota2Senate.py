class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = 0, 0
        while len(set(senate)) > 1:
            stack = []
            for s in senate:
                if s == 'R':
                    if r > 0:
                        r -= 1
                    else:
                        stack.append(s)
                        d += 1
                else:
                    if d > 0:
                        d -= 1
                    else:
                        stack.append(s)
                        r += 1

            if r + d >= len(stack):
                senate = [stack[-1]]
            senate = str(''.join(stack))        

        return "Radiant" if senate[0] == 'R' else "Dire"
                

