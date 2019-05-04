'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

from collections import Counter
class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		countS = Counter(s)
		countT = Counter(t)
		lenT = len(t)

		for char in countT.keys():
			if countS[char] < countT[char]:
				return ""

		countWin = Counter()
		count = 0

		# Initialize the sliding window
		begin = 0
		end = 0
		minwin = [0, len(s)]
		while end < len(s) :
			countWin[s[end]] += 1
			if countWin[s[end]] <= countT[s[end]]: # The current character is included in T
				count += 1
			
			if s[begin] == s[end]:
				while countWin[s[begin]] > countT[s[begin]]:
					countWin[s[begin]] -= 1
					begin += 1

			if count == lenT:
				minwin = [begin, end+1] if (end - begin < minwin[1] - minwin[0]) else minwin

			print minwin
			end += 1
		
		return s[minwin[0]: minwin[1]] if minwin[1] > minwin[0] else s[minwin[0]]

obj = Solution()
print obj.minWindow('acbbaca','aba')
print obj.minWindow("ADOBECODEBANCEE", "ABC")
print obj.minWindow("bb", "a")
print obj.minWindow("a", "a")
print obj.minWindow("ab", "a")
print obj.minWindow("acde", "acde")