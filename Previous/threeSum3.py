class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums = sorted(nums)
		ans = []

		i = 0
		while i<len(nums)-2 and nums[i]<=0:
			l = i + 1
			r = len(nums) - 1
			print i, l, r

			while l<r:
				summation = nums[i] + nums[l] + nums[r]
				if summation>0:
					while l<r and nums[r] == nums[r-1]:
						r -= 1
					r -= 1
				elif summation<0:
					while l<r and nums[l] == nums[l+1]:
						l += 1
					l += 1
				else:
					ans.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l] == nums[l+1]:
						l += 1
					while l<r and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -= 1

			while i<len(nums)-2 and nums[i] == nums[i+1]:
				i += 1
			i += 1

		return ans



if __name__ == '__main__':
	s = Solution()
	print s.threeSum([-1, 0, 1, 2, -1, -4])      