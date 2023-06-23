def solve(k, n, dic, height = 1):
    if k == 1:
        if n + height < 10:
            return [[n]]
        else:
            return []

    output = []
    for i in range(min(9 - height, n//k) + 1):
        #print(k, n, i)

        temp = [[i] + [i + n for n in s] for s in solve(k - 1, n - (i * k), dic, height + i + 1)]
        output += temp
    return output
        


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dic = {}

        for i in range(1, 10):
            dic[i] = (i * (i + 1))//2

        free = n - dic[k]
        if free < 0:
            return []

            
        output = solve(k, free, dic)

        for o in output:
            for i, n in enumerate(o):
                o[i] += i + 1

        

        


        return output
