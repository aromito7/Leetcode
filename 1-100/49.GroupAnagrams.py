class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = {}

        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in groups:
                groups[sort] = []
            groups[sort] += [s]
        return [groups[key] for key in groups]
            
