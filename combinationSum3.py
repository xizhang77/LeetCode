def dfs(nums, target, lenpath, start, path, ans):
	if target == 0 and len(path)== lenpath:
		ans.append(path)
		return
	elif len(path) and target < path[-1]:
		return

	for i in range(start, len(nums)):
		dfs(nums, target - nums[i], lenpath, i+1, path + [nums[i]], ans)

def combinationSum3(k, n):
	"""
	:type k: int
	:type n: int
	:rtype: List[List[int]]
	"""

	nums = range(1, 10)

	ans = []
	dfs(nums, n, k, 0, [], ans)

	return ans


print combinationSum3(3, 9)


