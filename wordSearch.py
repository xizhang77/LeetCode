'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution(object):
	def dfs(self, board, word, path, last_i, last_j, m, n):
		if not word:
			return True

		connect = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]

		for dirt in connect:
			ii = last_i + dirt[0]
			jj = last_j + dirt[1]
			if ii >= 0 and jj>= 0 and ii < m and jj < n and board[ii][jj] == word[0] and [ii, jj] not in path:
				if self.dfs( board, word[1:], path + [[ii, jj]], ii, jj, m, n):
					return True
		
		return False

	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		if not board:
			return len(word) == 0
		if not word:
			return True

		m = len(board)
		n = len(board[0])

		for i in range(m):
			for j in range(n):
				if board[i][j] == word[0]:
					if self.dfs( board, word[1:], [ [i, j] ], i, j, m, n):
						return True
		return False

obj = Solution()
print obj.exist( [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
