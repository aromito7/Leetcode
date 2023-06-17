class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        nums = [str(i + 1) for i in range(n)]
        factorial = math.factorial(n)
        output = ''

        while nums:
            factorial //= len(nums)
            cur = k // factorial
            k %= factorial
            output += nums[cur]
            nums = nums[:cur] + nums[cur + 1:]
        
        return output
        
