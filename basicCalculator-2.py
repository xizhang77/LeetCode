# -*- coding: utf-8 -*-
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s = s.replace(' ', '')

		if not s:
			return 0
		if s.isdigit():
			return int(s)

		num = ''
		op = '+'
		stack = []

		for i in range(len(s)):
			if s[i].isdigit():
				num += s[i]

			if not s[i].isdigit() or i == len(s) - 1:
				if op == '+':
					stack.append(int(num))
				elif op == '-':
					stack.append(- int(num) )
				elif op == '*' or op == '/':
					prenum = stack.pop()
					if prenum < 0:
						prenum = - prenum
						temp = prenum * int(num) if op == '*' else prenum / int(num)
						temp = - temp
					else:
						temp = prenum * int(num) if op == '*' else prenum / int(num)
					print prenum, int(num), temp
					stack.append(temp)
				op = s[i]
				num = ''
		
		print stack
		ans = 0
		while stack:
			ans += stack.pop()

		return ans

obj = Solution()
# print obj.calculate(" 34 + 5/2 - 3*2*3 ")
print obj.calculate(" 14 - 3/2 ")

