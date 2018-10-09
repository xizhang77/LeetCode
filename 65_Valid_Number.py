# -*- coding: utf-8 -*-

'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one. 
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. 
If you still see your function signature accepts a const char * argument, 
please click the reload button to reset your code definition.
'''

'''
这道题需要判断：
1.正负号：只可以出现在数字之前，e之后
2.数字：整数或者带小数点
3.e：只可以出现在两个数字之间, 即前面必须有数字，而且后面数字为整数
4.空格：只可以在开始或者结尾，在中间为False
'''

class Solution(object):
	def isNumber(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		s = s.strip()
		s = s.lower()

		isNum, isDot, isExp = False, False, False

		if s and s[0] in ['+', '-']:
			s = s[1:]

		for i in range(len(s)):
			print s[i], isNum, isDot, isExp
			if s[i].isdigit():
				isNum = True
			elif s[i] == '.':
				if isDot or isExp:
					return False
				isDot = True
			elif s[i] == 'e':
				if isExp or not isNum:
					return False
				isExp, isNum = True, False
			elif s[i] in ['+', '-']:
				if s[i-1] != 'e':
					return False
			else:
				return False

		return isNum


obj = Solution()
# print obj.isNumber('  2e10   ')
print obj.isNumber("92e1740e91")