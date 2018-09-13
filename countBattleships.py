class Solution(object):
	def countBattleships(self, board):
		"""
		:type board: List[List[str]]
		:rtype: int
		"""
		count = 0

		if board == []:
			return 0


		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 'X':
					if i == 0:
						if j == 0 or board[i][j-1] == '.':
							count += 1
					else:
						if (j == 0 and board[i-1][j] == '.') or (board[i-1][j] == '.' and board[i][j-1] == '.'):
							count += 1

		return count


s = Solution()
print s.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
        