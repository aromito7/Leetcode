class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = [[], []]
        set1 = set(nums1)
        set2 = set(nums2)

        # print(nums1, set1)
        # print(nums2, set2)

        for num in set1:
            if num not in set2:
                output[0].append(num)
            
        for num in set2:
            if num not in set1:
                output[1].append(num)

        return output
