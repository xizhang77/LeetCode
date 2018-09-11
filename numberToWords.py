class Solution(object):
	def __init__(self):
		self.under20 = [" " ," One" ," Two" ," Three" ," Four" ," Five" ," Six" ," Seven" ," Eight" ," Nine" ," Ten" ," Eleven" ," Twelve" ," Thirteen" ," Fourteen" ," Fifteen" ," Sixteen" ," Seventeen" ," Eighteen" ," Nineteen" ]
		self.tens = [" " ," Ten" ," Twenty" ," Thirty" ," Forty" ," Fifty" ," Sixty" ," Seventy" ," Eighty" ," Ninety" ]
		self.thousands = [" ", " Thousand", " Million", " Billion" ]

	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		""" 
		if num == 0:
			return " Zero" 
		ans = ""
		for i in range(len(self.thousands)):
			if num % 1000 !=0:
				ans = self.solver1000( num % 1000 ) + self.thousands[i] + ans
			num = num/1000

		return ans.strip()


	def solver1000(self, num):
		if num<20:
			return self.under20[num]
		elif num<100:
			return self.tens[ num / 10 ] + self.under20 [ num % 10 ] 
		else:
			return self.under20[ num / 100 ] + " Hundred" + self.solver1000( num % 100 )


if __name__ == '__main__':
	S = Solution()
	print S.numberToWords( 2000 )