class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        output = 0

        left_right = [[h] for h in height]
        left_right[0] += [0]
        left_max = height[0]
        right_max = height[-1]
        for i in range(1, len(height)):
            left_right[i] += [left_max]
            if height[i] > left_max:
                left_max = height[i]
        
        left_right[-1] += [0]
        for i in range(len(height) - 2, -1, -1):
            left_right[i] += [right_max]
            if height[i] > right_max:
                right_max = height[i]

        for lr in left_right:
            output += max(0, min(lr[1], lr[2]) - lr[0])

        # max_height = 0
        # maxes = [0, height[0]]

        # increasing = True

        # i = 1
        # while i < len(height):

        #     h = height[i]
        #     increasing = (h == height[i - 1] and increasing) or h > height[i - 1]
        #     print(i, height[i], increasing)
        #     pos = i + 1
        #     is_local_maximum = increasing
            
        #     if increasing:
        #         while pos < len(height):
        #             if height[pos] > h:
        #                 is_local_maximum = False
        #                 break
        #             elif height[pos] < h:
        #                 break
        #             pos += 1
        #             i += 1
        #     if is_local_maximum:
        #         maxes += [[i, h]]
        #     i += 1

        # maxes[0] += [0]
        # for i in range(1, len(maxes)):
        #     prev = maxes[i - 1]
        #     maxes[i] += [max(prev[1], prev[2])]


        # maxes[-1] += [0]
        # for i in range(len(maxes) - 2, -1, -1):
        #     nex = maxes[i + 1]
        #     maxes[i] += [max(nex[1], nex[3])]

        # temp = []
        # for m in maxes:
        #     if m[1] > m[2] or m[1] > m[3]:
        #         temp += [m]

        # maxes = temp
        
        # for i, curr in enumerate(maxes):
        #     if i == 0: continue
        #     prev = maxes[i - 1]
        #     water_level = min(prev[1], curr[1])
        #     for val in height[prev[0] + 1: curr[0]]:
        #         output += max(water_level - val, 0)
        return output
