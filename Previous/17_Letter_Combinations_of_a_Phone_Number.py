class Solution(object):
	def __init__(self):
		self.letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

	def dfs(self, digits, path, ans):
		if not digits:
			ans.append(path)
			return
		for char in self.letter[digits[0]]:
			self.dfs( digits[1:], path + char, ans)

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		ans = []
		self.dfs( digits, '', ans)
		return ans

obj = Solution()
print obj.letterCombinations('23')