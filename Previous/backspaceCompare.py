# -*- coding: utf-8 -*-

'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

'''

class Solution(object):
	def backspaceCompare(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: bool
		"""
		stacks = []
		stackt = []

		i, j = 0, 0

		while i < len(S) or j < len(T):
			if i < len(S):
				if S[i] == '#':
					if stacks:
						stacks.pop()
				else:
					stacks.append(S[i])
				i += 1
			if j < len(T):
				if T[j] == '#':
					if stackt:
						stackt.pop()
				else:
					stackt.append(T[j])
				j += 1

		return stacks == stackt

obj = Solution()
print obj.backspaceCompare("a##c", "#a#c")
