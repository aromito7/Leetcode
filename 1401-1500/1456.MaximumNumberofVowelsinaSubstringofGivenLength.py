class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        output = 0
        cur = 0

        for char in s[:k]:
            if char in vowels:
                cur += 1
        
        output = cur

        for i in range(k, len(s)):
            char = s[i]
            prev = s[i - k]

            if prev in vowels:
                cur -= 1

            if char in vowels:
                cur += 1
                output = max(output, cur)
        
        return output


