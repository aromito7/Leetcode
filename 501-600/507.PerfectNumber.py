class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 1

        root = int(num ** .5)

        for i in range(2, root + 1):
            if num % i == 0:
                total += i + (num // i)

        if root ** 2 == num:
            total += root

        if num == total:
            return True

        return False

