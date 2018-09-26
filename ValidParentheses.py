'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if not s:
			return True
		n = len(s)
		if n%2:
			return false

		ddict = {'(':')', '{':'}', '[':']'}
		stack = []
		for i in range(len(s)):
			if s[i] in ddict.keys():
				stack.append(s[i])
			elif s[i] in ddict.values():
				if not stack:
					return False
				if ddict[stack.pop()] != s[i]:
					return False
			else:
				return 'Error Input'

		if stack:
			return False

		return True



obj = Solution()
print obj.isValid("{[]}")
print obj.isValid("((")
print obj.isValid("{[]}]]")