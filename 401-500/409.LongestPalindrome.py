class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 0
        letters = set()
        for letter in s:
            if letter in letters:
                letters.remove(letter)
                output += 2
            else:
                letters.add(letter)

        if letters:
            output += 1

        return output
