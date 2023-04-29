class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs[0]) == 0:
            return ''
        output = ''
        length = len(strs)

        i = 0
        while True:
            if i >= len(strs[0]):
                return output
            cur = strs[0][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != cur:
                    return output
            
            output += cur
            i += 1
            

        return output
