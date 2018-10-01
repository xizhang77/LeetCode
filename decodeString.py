# -*- coding: utf-8 -*-
'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, 
k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution(object):
	def decodeString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s:
			return ""

		currnum = ''
		currstring = ''
		stack = []
		for char in s:
			if char == '[':
				stack.append(currstring)
				stack.append(currnum)
				currstring = ''
				currnum = ''
			elif char == ']':
				prenum = stack.pop()
				prestring = stack.pop()
				currstring = prestring + int(prenum) * currstring
			elif char.isdigit():
				currnum += char
			else:
				currstring += char

		return currstring



obj = Solution()
print obj.decodeString("3[a2[c]2[e]]")
# print obj.decodeString('2[abc]3[cd]ef')

# print obj.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
