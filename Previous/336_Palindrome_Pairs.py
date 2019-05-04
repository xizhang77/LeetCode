'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, 
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: ["a", ""]
Output: [[0,1],[1,0]]
'''

class Solution(object):
	def palindromePairs(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[int]]
		"""
		ans = []
		if not words:
			return ans

		hashMap = {}
		n = len(words)
		for i in range(n):
			hashMap[ words[i] ] = i

		for i in range(n):
			word = words[i]
			for j in range(len(word)+1):
				left = word[:j]
				right = word[j:]
				print left, right
				if right == right[::-1] and left[::-1] in hashMap:
					idx = hashMap[left[::-1]]
					if i != idx and [i, idx] not in ans:
						ans.append([i, idx])

				if left == left[::-1] and right[::-1] in hashMap:
					idx = hashMap[right[::-1]]
					if i != idx and [idx, i] not in ans:
						ans.append([idx, i])

		return ans


obj = Solution()
print obj.palindromePairs( ["abcd","dcba","lls","s","sssll"] )
# print obj.palindromePairs( ["aa", ""])
