class Solution:
    def exist(self, board, word):
        start = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    start.append((i,j))
        for s in start:
            stp = board[s[0]][s[1]]
            print(stp)

sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
sol.exist(board,word)
