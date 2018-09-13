class Solution(object):
	def constructMaximumBinaryTree(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		Implement on Leetcode directly and it works (with pre-defind TreeNode)
		"""
		ans = []

		if len(nums) == 0:
			print 'null'
		else:
			maxvalue = max(nums)
			maxindex = nums.index(maxvalue)
			self.constructMaximumBinaryTree(nums[maxindex+1:])
			self.constructMaximumBinaryTree(nums[:maxindex])
			print maxvalue


if __name__ == '__main__':
	S = Solution()
	S.constructMaximumBinaryTree([3,2,1,6,0,5])