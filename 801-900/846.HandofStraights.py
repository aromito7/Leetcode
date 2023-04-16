class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        length = len(hand)

        if length % groupSize > 0:
            return False

        dic = defaultdict(lambda: 0)

        for card in hand:
            dic[card] += 1



        for key in sorted(dic):
            if dic[key] == 0:
                continue
            for delta in range(1, groupSize):
                if key + delta not in dic or dic[key+delta] < dic[key]:
                    print(key, delta, dic[key+delta], dic[key])
                    return False
                dic[key + delta] -= dic[key]


        return True
