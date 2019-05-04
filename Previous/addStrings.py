'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		num1 = num1[::-1]
		num2 = num2[::-1]

		residual = 0

		ans = ''

		while num1 and num2:
			curr = int(num1[0]) + int(num2[0]) + residual
			ans += str( curr%10 )
			residual = curr/10
			num1 = num1[1:]
			num2 = num2[1:]

		nums = num1 if num1 else num2

		while nums:
			curr = int(nums[0]) + residual
			ans += str( curr%10 )
			residual = curr/10
			nums = nums[1:]

		if residual:
			ans += str(residual)

		return ans[::-1]

obj = Solution()
print obj.addStrings('8', '99999992')
print obj.addStrings('', '')
print obj.addStrings('', '2')