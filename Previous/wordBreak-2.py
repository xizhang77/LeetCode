# -*- coding: utf-8 -*-
'''
It's LTE because of one annoying testcase... Will try later...
'''


'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

class Solution(object):
	def dfs(self, s, Dict, path, ans):
		if not s:
			ans.append( path )
			return
		char = ''
		for i in range(len(s)):
			char += s[i]
			if char in Dict:
				self.dfs( s[i+1:], Dict, path + [char], ans )

	def check(self, s, Dict):
		n = len(s)
		dp = [True] + [False]*n

		for i in range(n):
			for j in range(i+1):
				if dp[j] and s[j: i+1] in Dict:
					dp[ i+1 ] = True
		return dp[n]

	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		ans = []

		if not s:
			return ans
		if set(s) - set("".join(wordDict)):
			return ans

		if self.check(s, wordDict):
			self.dfs( s, wordDict, [], ans)
			return [ " ".join(item) for item in ans ]
		else:
			return ans


obj = Solution()
print obj.wordBreak( "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
# print obj.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        