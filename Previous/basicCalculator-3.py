# -*- coding: utf-8 -*-

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . 
The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

'''

class Solution(object):
	def retrival(self, op, num, stack):
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
			stack.append(temp)

		return stack

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

		stack = []
		num = ''
		op = '+'
		for i in range(len(s)):
			# print s[i]
			if s[i].isdigit():
				num += s[i]
			if not s[i].isdigit() or i == len(s) - 1:
				if s[i] == '(':
					stack.append(op)
					op = '+'
				elif s[i] == ')':
					if num:
						stack = self.retrival(op, num, stack)
					tempsum = 0
					while isinstance( stack[-1], int):
						tempsum += stack.pop()
					op = stack.pop()
					stack = self.retrival(op, tempsum, stack)
				else:
					if num:
						stack = self.retrival(op, num, stack)
					op = s[i]
				num = ''
			# print stack

		ans = 0
		while stack:
			ans += stack.pop()

		return ans

obj = Solution()
# print obj.calculate("2*(5+5*2)/3+(6/2+8)")
# print obj.calculate("(2+6* 3+5- (3*14/7+2)*5)+3")

print obj.calculate("(1-(3-4))")
