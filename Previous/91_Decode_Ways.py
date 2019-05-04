class Solution(object):		
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if len(s) == 0 or s[0] == '0':
			return 0
		if len(s) == 1:
			return 1

		dp = [1,1]

		for i in range(2, len(s)+1):
			if int(s[i-2: i])>10 and int(s[i-2: i])<=26 and int(s[i-2: i]) != 20:
				dp.append( dp[i-2] + dp[i-1] )
				print dp
			elif int(s[i-2: i])==10 or int(s[i-2: i])==20:
				dp.append( dp[i-2] )
				print dp
			elif s[i-1] != '0':
				dp.append( dp[i-1] )
				print dp
			else:
				return 0

		return dp[ len(s) ]



if __name__ == '__main__':
	s = Solution()
	print s.numDecodings("017")