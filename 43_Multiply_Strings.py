'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
	def mult(self, num1, num):
		if num == '0':
			return '0'
		res = 0
		ans = []
		for i in range(len(num1)-1, -1, -1):
			temp = int(num) * int(num1[i]) + res
			res = temp/10
			ans = [str(temp%10)] + ans
		if res:
			ans = [str(res)] + ans
		return int(''.join(ans))

	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		if num1 == '0' or num2 == '0' or not num1 or not num2:
			return '0'

		if len(num1) < len(num2):
			num1, num2 = num2, num1
		ans = 0
		level = 1
		for i in range(len(num2)-1, -1, -1):
			ans += self.mult(num1, num2[i]) * level
			level *= 10

		return str(ans)

obj = Solution()
# print obj.multiply("123", "456")
print obj.multiply("9", "9")


