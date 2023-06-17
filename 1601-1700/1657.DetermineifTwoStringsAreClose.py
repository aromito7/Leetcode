def convert(word1):
    dic = defaultdict(lambda:0)
    for char in word1:
        dic[char] += 1

    return list(dic.values())





class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
            
        return sorted(convert(word1)) == sorted(convert(word2))
