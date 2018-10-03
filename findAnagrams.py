'''
This one is LTE... 
'''
class Solution(object):
	def findAnagrams(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		ans = []
		for i in range(len(s)-len(p)+1):
			if sorted(s[i:i+len(p)]) == sorted(p):
				ans.append(i)

		return ans

S = Solution()
print S.findAnagrams("aabaab", "aab")


'''
AC solution
'''

from collections import Counter
class BetterSolution(object):
	def findAnagrams(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		ans = []
		pCounter = Counter(p)
		sCounter = Counter(s[:len(p)-1])
		for i in range(len(s)-len(p)+1):
			sCounter[ s[i+len(p)-1] ] += 1
			print sCounter
			if sCounter == pCounter:
				ans.append(i)
			sCounter[s[i]] -= 1
			if sCounter[ s[i] ] == 0:
				del sCounter[ s[i] ]

		return ans

obj = BetterSolution()
print obj.findAnagrams("cbaebabacd", "abc")