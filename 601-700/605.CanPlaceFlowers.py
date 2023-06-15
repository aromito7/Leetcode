class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        spaces = [1]

        for f in flowerbed:
            if f == 1:
                spaces.append(0)
            else:
                spaces[-1] += 1

        spaces[-1] += 1

        return sum([(s - 1) // 2 for s in spaces]) >= n
        
