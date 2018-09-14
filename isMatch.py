class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if p == "":
			return (s == "")
		
		if len(p) == 1:
			if s == p or ( p == '.' and len(s) == 1):
				return True
			else:
				return False

		if p[-1] != '*' and p[-1] != '.' and p[-1] not in s:
			return False
		
		if p[1] != '*':
			if s != '' and (s[0] == p[0] or p[0] == '.' ):
				return self.isMatch( s[1:], p[1:] )
			else:
				return False
		else:
			while ( s != '' and (s[0] == p[0] or p[0] == '.' )):
				if self.isMatch( s, p[2:] ):
					return True
				s = s[1:]
			return self.isMatch( s, p[2:] )


S = Solution()
'''
print S.isMatch("aa", "a")
print S.isMatch("aa", "a*")
print S.isMatch("ab", ".*")
print S.isMatch("aab", "c*a*b")
print S.isMatch("mississippi", "mis*is*p*.")

print S.isMatch("aaa", "a*a")
print S.isMatch("a", "ab*")
'''
print S.isMatch("ab", ".*c")



