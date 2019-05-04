'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0

		stack = []
		ans = 0
		for i in range(len(s)):
			if s[i] not in stack:
				stack += [s[i]]
			else:
				ans = max(ans, len(stack))
				idx = stack.index(s[i])
				stack = stack[idx+1:] + [s[i]]

		return max(ans, len(stack))

obj = Solution()
print obj.lengthOfLongestSubstring("abcabcbb")
