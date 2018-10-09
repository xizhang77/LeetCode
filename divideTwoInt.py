# -*- coding: utf-8 -*-

'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

'''

class Solution(object):
	'''
	The following solution is LTE when dividend = 2147483648 (MAX + 1). 
	'''
	def divide_slow(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		MAX = float('inf')

		sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
		
		ans = 0

		dividend, divisor = abs(dividend), abs(divisor)

		while dividend >= divisor:
			dividend -= divisor
			ans += 1

		ans = sign * ans

		if ans > MAX:
			return MAX
		else:
			return ans

	"""
	为了加速运算，可以依次将被除数减去1，2，4，8，..倍的除数。所以这里用移位来加速。 (1<<2 = 4; 3<<1 = 9...)
	"""
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		MAX = float('inf')

		sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
		
		ans = 0

		dividend, divisor = abs(dividend), abs(divisor)

		while dividend >= divisor:
			k = 0
			temp = divisor
			while dividend >= temp:
				dividend -= temp
                ans += 1 << k
                temp <<= 1
                k += 1 

		ans = sign * ans

		if ans > MAX:
			return MAX
		else:
			return ans


obj = Solution()
print obj.divide( 7, -3 )