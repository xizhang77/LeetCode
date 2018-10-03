'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
def dfs(nums, target, start, path, ans):
	if target==0:
		ans.append(path)
		return
	elif target<0:
		return

	for i in range(start, len(nums)):
		dfs(nums, target - nums[i], i, path + [nums[i]], ans)


def combinationSum(candidates, target):
	"""
	:type candidates: List[int]
	:type target: int
	:rtype: List[List[int]]
	"""
	ans = []
	dfs(candidates, target, 0, [], ans)

	return ans


print combinationSum([2,3,5], 8)


'''
Better version. (48ms vs 108ms)
'''
class Solution(object):
	def dfs(self, nums, target, path, ans):
		if target == 0:
			ans.append( list(path) )
			path = []
			return
		else:
			for i in range(len(nums)):
				if target - nums[i] < 0:
					break
				self.dfs( nums[i:], target - nums[i], path + [nums[i]], ans)
	def combinationSum(self, candidates, target):
        ans = []
		self.dfs( sorted(candidates), target, [], ans)
		return ans

obj = Solution()
print obj.combinationSum()


        