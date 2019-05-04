# -*- coding: utf-8 -*-
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

'''

class Solution(object):
	def dfs(self, letterset, path, ans):
		if not len(letterset):
			ans.append( path )
			return

		for i in range(len(letterset[0])):
			self.dfs( letterset[1:], path + letterset[0][i], ans)

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		match = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
		ans = []
		if not digits:
			return ans

		letterset = []
		for char in digits:
			letterset.append(match[char])
		print letterset

		self.dfs( letterset, '', ans)
		return ans

obj = Solution()
print obj.letterCombinations('223')