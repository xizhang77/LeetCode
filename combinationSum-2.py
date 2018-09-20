def dfs(nums, target, start, path, ans):
    if target == 0 :
        ans.append(path)
        return
    elif len(path) and target < path[-1]:
        return

    for i in range(start, len(nums)):
        if i != start and nums[i]==nums[i-1]:
            i += 1
        else:
            dfs(nums, target - nums[i], i+1, path + [nums[i]], ans)

def combinationSum2(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        ans = []
        dfs(candidates, target, 0, [], ans)

        return ans

print combinationSum2([10,1,2,7,6,1,5], 8)