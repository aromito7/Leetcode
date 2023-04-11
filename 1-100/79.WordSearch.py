def solve(y, x, chain, board, end):
    if len(chain) + 1 not in board[y][x]:
        return False
    yx = '{},{}'.format(y,x)
    if yx in chain:
        return False


    if len(chain)  + 1 == end:
        return True

    if solve(y+1, x, chain + [yx], board, end) or solve(y-1, x, chain + [yx], board, end) or solve(y, x+1, chain + [yx], board, end) or solve(y, x-1, chain + [yx], board, end):
        return True

    return False


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        dic = {}

        for i, letter in enumerate(word):
            if letter not in dic:
                dic[letter] = [i + 1]
            else:
                dic[letter] += [i + 1]
        
        
        board = [[[0]] * (len(board[0]) + 2)]+[[[0]]+[dic[letter] if letter in dic else [0] for letter in row]+[[0]] for row in board] + [[[0]] * (len(board[0]) + 2)]

        print(board)

        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if solve(y, x, [], board, len(word)):
                    return True


        return False
