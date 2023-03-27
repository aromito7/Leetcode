class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        start = 0
        width = len(s1)

        dic1, dic2 = {}, {}

        for i in range(width):
            if s1[i] not in dic1:
                dic1[s1[i]] = 0
            dic1[s1[i]] += 1

            if s2[i] not in dic2:
                dic2[s2[i]] = 0
            dic2[s2[i]] += 1
        
        if dic1 == dic2:
            return True

        while start + width < len(s2):
            nex = s2[start + width]
            pre = s2[start]

            if nex not in dic2:
                dic2[nex] = 1
            else:
                dic2[nex] += 1

            if dic2[pre] == 1:
                dic2.pop(pre)
            else:
                dic2[pre] -= 1

            if dic1 == dic2:
                return True
            start += 1


        print(dic1, dic2)

        return False

