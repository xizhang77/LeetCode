'''
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
'''

from difflib import ndiff
class Solution(object):
	def isOneEditDistance(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		len_s, len_t = len(s), len(t)
		if len_s < len_t:
			s, t= t, s
			len_s, len_t = len_t, len_s

		if len_s - len_t > 1:
			return False
		elif len_s == len_t:
			for i in range(len_s):
				if s[i] == t[i]:
					continue
				else:
					return s[i+1:] == t[i:]
			# If there is no editing at all, return false
			return False
		else:
			for i in range(len_t):
				if s[i] == t[i]:
					continue
				else:
					return s[i+1:] == t[i]
			return True

obj = Solution()
print obj.isOneEditDistance( "1203", "1211")
print obj.isOneEditDistance( "ab", "acb")


