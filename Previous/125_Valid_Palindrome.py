'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
import re

class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		if not s or len(s) == 1:
			return true

		cleaned = re.findall(r'[a-zA-Z0-9+]', s)
		print cleaned

		if len(cleaned) == 1:
			return False

		i = 0
		j = len(cleaned) - 1
		while i < j:
			print cleaned[i].lower(), cleaned[j].lower()
			if cleaned[i].lower() == cleaned[j].lower():
				i += 1
				j -= 1
			else:
				return False

		return True 

obj = Solution()
print obj.isPalindrome("0P")
# print obj.isPalindrome("race a car")
# print obj.isPalindrome("A man, a plan, a canal: Panama")
        