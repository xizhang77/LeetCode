'''
This one is LTE, try another solution...
'''

'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

class Solution(object):
	def validPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		return self.detect(s, 0)

	def detect(self, s, mark):
		print s, mark

		if not s or len(s) == 1:
			return True

		i = 0
		j = len(s) - 1

		if s[i] == s[j]:
			return self.detect(s[i+1: j], mark)
		else:
			print 'enter first else'
			if not mark:
				return (self.detect(s[i+1: j+1], 1) or self.detect(s[i: j], 1))
			else:
				return False

		return True

obj = Solution()
print obj.validPalindrome("eeccccbebaeeabebccceea")

