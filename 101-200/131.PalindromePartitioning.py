def partition(remaining, palindromes):
    output = []
    if len(palindromes) == 0:
        return output
    for p in palindromes[0]:
        l = len(p)
        temp = partition(remaining[l:], palindromes[l:])
        if len(temp) == 0:
            output += [[p]]
        else:
            output += [[p] + n for n in temp]

    return output
    

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        s = ''.join([letter.encode('ascii') for letter in s])
        palindromes = [[] for i in range(len(s))]

        for i, letter in enumerate(s[:-1]):
            palindromes[i] += [letter]
            delta = 1
            
            while 0 <= i - delta < i + delta < len(s) and s[i - delta] == s[i + delta]:
                palindromes[i - delta] += [''.join(s[i-delta:i+delta + 1])]
                delta += 1
            delta = 0

            if s[i] == s[i + 1]:
                while 0 <= i - delta < i + delta + 1 < len(s) and s[i - delta] == s[i + delta + 1]: 
                    palindromes[i - delta] += [''.join(s[i-delta:i+delta + 2])]
                    delta += 1
        palindromes[-1] = [s[-1]]
        print(s, palindromes)
        return partition(s, palindromes)
