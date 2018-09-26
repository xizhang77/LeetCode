'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

import re

class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		if not s:
			return 0
		if s.isdigit():
			return int(s)

		s = s.replace(' ', '')
		print s

		ans = 0

		sign = 1 # Maintain the sign for next calculation
		num = ''  # 
		stack = []
		for char in s:
			if char.isdigit():
				num += char
			else:
				if num:
					ans += sign*int(num)
					num = ''
				if char == '-':
					sign = -1
				elif char == '+':
					sign = 1
				elif char == '(':
					stack.append([ans, sign])
					sign = 1
					ans = 0
				elif char == ')':
					temp = stack.pop()
					ans = temp[0] + temp[1]*ans
					sign = 1
		if num:
			ans += sign*int(num)

		return ans

obj = Solution()
print obj.calculate("(1+(4+5+2)-3)+(6+8)")
# print obj.calculate("1-1")
print obj.calculate("34 + 25 - 77")
print obj.calculate(" 45 - (7 + (2 - 5) -3) + 6 ")