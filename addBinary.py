class Solution(object):
	def addBinary(self, a, b):
        """
		:type a: str
		:type b: str
		:rtype: str
		"""
		return bin(int(a, 2) + int(b, 2))[2:]



if __name__ == '__main__':
	s = Solution()
	s.addBinary("1010", "1011")