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


        