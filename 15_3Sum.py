class Solution(object):

	def dfs(self, nums, i, ans, subset):
		if len(subset) == 3 and sum(subset) == 0 and subset not in ans:
			ans.append(subset)
			return
		if (-sum(subset)) not in nums or len(subset) > 3:
			return

		for j in range(i, len(nums)):
			self.dfs(nums, j+1, ans, subset+ [nums[j]])


	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		ans = []
		self.dfs(sorted(nums), 0, ans, [])

		return ans

# Another solution without dfs
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) < 3:
            return ans
        i = 0
        nums = sorted(nums)
        n = len(nums)
        while i < n:
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left< right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    while left< right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                else:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        
        return ans
                    
                    
                    


if __name__ == '__main__':
	s = Solution()
	print s.threeSum([-13,11,11,0,-5,-14,12,-11,-11,-14,-3,0,-3,12,-1,-9,-5,-13,9,-7,-2,9,-1,4,-6,-13,-7,10,10,9,7,13,5,4,-2,7,5,-13,11,10,-12,-14,-5,-8,13,2,-2,-14,4,-8,-6,-13,9,8,6,10,2,6,5,-10,0,-11,-12,12,8,-7,-4,-9,-13,-7,8,12,-14,10,-10,14,-3,3,-15,-14,3,-14,10,-11,1,1,14,-11,14,4,-6,-1,0,-11,-12,-14,-11,0,14,-9,0,7,-12,1,-6])
      