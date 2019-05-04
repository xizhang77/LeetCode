# -*- coding: utf-8 -*-

'''
大概思路如下：

- 若p为空，s也为空，返回true，反之返回false

- 若p的长度为1，若s长度也为1，且相同或是p为'.'则返回true，反之返回false

- 若p的第二个字符不为*，若此时s为空返回false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配

- 若p的第二个字符为*，若s不为空且字符匹配，调用递归函数匹配s和去掉前两个字符的p，若匹配返回true，否则s去掉首字母

- 返回调用递归函数匹配s和去掉前两个字符的p的结果
'''


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
				
		# The following if is used for purning. The program is still working without it.
		# But the running time can be improved from 1000ms to 110ms with pruning
		if p[-1] != '*' and p[-1] != '.' and p[-1] not in s:
			return False
		
		if p[1] != '*':
			if s != '' and (s[0] == p[0] or p[0] == '.' ):
				return self.isMatch( s[1:], p[1:] )
			else:
				return False
		else:
			while ( s != '' and (s[0] == p[0] or p[0] == '.' )):
				if self.isMatch( s, p[2:] ):  #For case "aaa", "a*a"
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



