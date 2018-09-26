# -*- coding: utf-8 -*-

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false

'''

class Solution(object):
	def isStrobogrammatic(self, num):
		"""
		:type num: str
		:rtype: bool
		"""

		if len(set(num) == set('01689')):
			return False

		p = 0
		q = len(num) - 1

		while p <= q:
			if (num[p] in set('018') and num[p] == num[q] ) or (num[p] == '6' and num[q] == '9') or (num[p] == '9' and num[q] == 6):
				p += 1
				q -= 1
			else:
				return False

		return True

obj = Solution()
print obj.isStrobogrammatic("6")
print obj.isStrobogrammatic("818")