# -*- coding: utf-8 -*-
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''

from collections import Counter
class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		cnt = Counter(s)
		print cnt.keys()
		print cnt.values()
		uniqchar = [ char for char in cnt.keys() if cnt[char] == 1]

		return min([ s.index(char) for char in uniqchar]) if uniqchar else -1

obj = Solution()
print obj.firstUniqChar("loveleetcode")
# print obj.firstUniqChar("ccc")