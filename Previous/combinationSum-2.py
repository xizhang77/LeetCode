'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''

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


'''
This version is much clear and efficient.
'''

class Solution(object):
    def dfs(self, nums, target, path, ans):
        if target == 0 and path not in ans:
            ans.append( path )
            return
        else:
            i = 0
            while i < len(nums):
                if target - nums[i] < 0:
                    break
                self.dfs( nums[i+1:], target - nums[i], path + [nums[i]], ans)
                while i< len(nums) - 1 and nums[i] == nums[i+1]:
                    i+=1
                i += 1
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs( sorted(candidates), target, [], ans)
        return ans



