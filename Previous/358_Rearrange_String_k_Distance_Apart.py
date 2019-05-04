# -*- coding: utf-8 -*-

'''
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
'''
from collections import Counter
class Solution(object):
	def rearrangeString(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: str
		"""
		if k == 0:
			return s

		count = Counter(s)
		stack = [ [count[key], key] for key in count.keys() ]
		stack.sort(key=lambda x: x[0]) # use pop() to get the highest frequency term

		# Find the char/chars with highest count. 
		max_count, char = stack.pop()
		while stack and stack[-1][0] == max_count:
			temp = stack.pop()[1]
			char += temp

		ans = [[char] for i in range(max_count)]
		res = len(s) - len(char) * max_count # Used to stop if res<k and stack
		if res == 0 and len(char) >= k:
			return "".join(sum(ans, []))
		elif res < (k-1)*(max_count-1):
			return ""

		# Later, padding the rest of the characters 
		pointer = 0
		while stack:
			if res < (k-1)*(max_count-1):
				return ""
			num_char, char = stack.pop()
			for i in range(num_char):
				ans[(i + pointer) % (max_count-1)] += char
			pointer = i + 1
			res -= num_char
			k = k-1 if k - 1 >= 0 else 0

		print ans
		return "".join(sum(ans, []))

obj = Solution()
print obj.rearrangeString("aabbcc", 2)
