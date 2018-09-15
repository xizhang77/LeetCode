'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Palindromic strings: 
'''

class Solution(object):
	def countSubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		count = 0

		for i in range(len(s)):
			count += 1 # character itself is a palindromic substring
			lpointer = i - 1
			rpointer = i + 1
			while lpointer >=0 and rpointer < len(s) and s[lpointer] == s[rpointer]:
				count += 1
				lpointer -= 1
				rpointer += 1

			lpointer = i
			rpointer = i + 1
			while lpointer >=0 and rpointer < len(s) and s[lpointer] == s[rpointer]:
				count += 1
				lpointer -= 1
				rpointer += 1


		return count

obj = Solution()
print obj.countSubstrings('aaa')