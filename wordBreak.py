'''
LTE again... Try DP instead of DFS (too many return in DFS, which boost the time complexity)
'''

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution(object):
	def dfs(self, s, Dict, path):
		if not s:
			return True
		char = ''
		for i in range(len(s)):
			char += s[i]
			if char in Dict:
				if self.dfs( s[i+1:], Dict, path + [char]):
					return True

		return False


	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		if not s:
			return True
		if set(s) - set("".join(wordDict)):
			return False
		return self.dfs( s, wordDict, [])

obj = Solution()
print obj.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])