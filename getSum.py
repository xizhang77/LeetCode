"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
"""

def getSum(a, b):
	"""
	:type a: int
	:type b: int
	:rtype: int
	"""
	MAX_INT = 0x7FFFFFFF
	MASK = 0x100000000
	while(b):
		carry = a & b
		a = (a ^ b) % MASK
		b = (carry << 1 ) % MASK
	return a if a <= MAX_INT else (~0 << 31) | a

print getSum(-1, 1)