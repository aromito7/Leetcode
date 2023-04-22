def contains(triplet, target, pos):
    for t in triplet:
        if t[pos] == target[pos]:
            return True

    return False    

class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        triplets = [t for t in triplets if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]]

        for i in range(3):
            if not contains(triplets, target, i):
                return False

        return True
