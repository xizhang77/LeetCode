'''
This solution is LTE... Try another version 
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