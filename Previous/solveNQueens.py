# -*- coding: utf-8 -*-

'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

class Solution(object):
	def check(self, n, rowNum, queenPath):
		blindList = []
		blindList += queenPath
		for i in range(len(queenPath)):
			if queenPath[i] + (rowNum - i) < n:
				blindList.append(queenPath[i] + (rowNum - i))
			if queenPath[i] - (rowNum - i) >= 0:
				blindList.append(queenPath[i] - (rowNum - i))
		return list(set(blindList))
	def dfs(self, n, rowNum, queenPath, ans):
		if rowNum == n:
			print "Append: ", queenPath
			ans.append(queenPath)
			return

		blindList = self.check(n, rowNum, queenPath)
		for i in range(n):
			if i not in blindList:
				self.dfs( n, rowNum + 1, queenPath + [i], ans)
		return

	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		ans = []
		self.dfs(n, 0, [], ans)
		res = []
		for item in ans:
			temp = [ '.'*n ]*n
			for row in range(n):
				temp_row = list(temp[row])
				temp_row = temp_row[:item[row]] + ['Q'] + temp_row[item[row]+1:]
				temp[row] = "".join(temp_row)
			res.append( temp )
		return res

obj = Solution()
print obj.solveNQueens(4)
        