class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        output = 1
        current = s[0]
        window = {s[0]: 1}
        i = 0


        #while i + output < len(s) and window[current] + k > output:


        while i + output < len(s):
            nex = s[i + output]
            if not nex in window:
                window[nex] = 1
            else:
                window[nex] += 1
            
            if window[nex] > window[current]:
                current = nex
            
            if window[current] + k > output:
                output += 1
            else:
                window[s[i]] -= 1
                i += 1
            


        return output
