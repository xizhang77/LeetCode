class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		zerocount = 0
		i = 0
		while i<len(nums):
			if nums[i] == 0:
				nums.pop(i)
				zerocount += 1
			else:
				i += 1
		for i in range(zerocount):
			nums.append(0)

		return nums


if __name__ == '__main__':
	s = Solution()
	print s.moveZeroes([0,0,1])
