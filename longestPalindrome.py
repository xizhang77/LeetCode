# -*- coding: utf-8 -*-

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''

class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		n = len(s)
		
		if len(set(s)) == 1:
			return s

		dp = [ [False for i in range(n)] for j in range(n) ]
		print dp

		ans = [0, 0]
		for j in range(n):
			dp[j][j] = True
			for i in range(j):
				if j - i == 1:
					dp[i][j] = (s[i] == s[j])
				else:
					dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])

				ans = [i, j] if dp[i][j] and j-i > ans[1] - ans[0] else ans
		print dp
		return s[ans[0]: ans[1] + 1]

obj = Solution()
print obj.longestPalindrome("cbbd")