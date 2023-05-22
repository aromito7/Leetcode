class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)


        if len(s) == 0:
            return True
        for i in range(len(t) - 1, -1, -1):

            if t[i] == s[-1]:
                s.pop()
                if len(s) == 0:
                    return True
        return False
