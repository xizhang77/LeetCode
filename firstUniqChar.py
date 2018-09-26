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
class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		cnt = {}

		for i in range(len(s)):
			if s[i] not in cnt.keys():
				cnt[s[i]] = [1, i]
			else:
				cnt[s[i]][0] += 1
			print cnt

		uniqchar = [ value[1] for value in cnt.values() if value[0] == 1]
		return min(uniqchar) if uniqchar else -1

obj = Solution()
# print obj.firstUniqChar("loveleetcode")
print obj.firstUniqChar("ccc")