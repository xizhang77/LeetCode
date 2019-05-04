# -*- coding: utf-8 -*-

'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]

'''

class Solution(object):
	def remove(self, ans, s, last_i, last_j, char):
		'''
		last_i: count['('] = count[')'] for s[: last_i]. Check the rest of the string
		last_j: the invalid parentheses is removed from s[: last_j]. Check the rest
		'''
		print s, last_i, last_j
		count = 0
		for i in range(last_i, len(s)):
			if s[i] == char[0]:
				count += 1
			elif s[i] == char[1]:
				count -= 1
			if count >= 0:
				continue

			for j in range(last_j, i + 1):
				if s[j] == char[1] and ( j == last_j or s[j-1] != char[1] ):
					self.remove( ans, s[:j] + s[j+1:], i, j, char )
			return

		reS = s[::-1]
		if char[0] == '(':
			self.remove( ans, reS, 0, 0, char[::-1])
		else:
			ans.append(reS)


	def removeInvalidParentheses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		ans = []
		char = ['(', ')']
		self.remove(ans, s, 0, 0, char)

		return ans

obj = Solution()
# print obj.removeInvalidParentheses('(()(()')

print obj.removeInvalidParentheses('()())()')