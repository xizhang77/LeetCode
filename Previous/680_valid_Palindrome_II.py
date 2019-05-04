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

# Solution2 is a little bit faster than the other (100ms vs 140ms)
class Solution2(object):
        
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 1:
            return True
        
        start, end = 0, len(s) - 1
        
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                s1 = s[:start] + s[start+1:]
                s2 = s[:end] + s[end+1:]
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                else:
                    return False
        
        return True

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

		while i < j:
			if s[i] != s[j]:
				print 'enter first else'
				if not mark:
					return (self.detect(s[i+1: j+1], 1) or self.detect(s[i: j], 1))
				else:
					return False
			else:
				i += 1
				j -= 1
		return True

obj = Solution()
print obj.validPalindrome("eeccccbebaeeabebccceea")

