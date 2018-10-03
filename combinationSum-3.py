'''
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

'''

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


'''
Another solution. (20ms vs 24ms)
'''

class Solution(object):
    def dfs(self, nums, Len, target, path, ans):
        if len(path) > Len:
            return
        if target == 0 and len(path) == Len:
            ans.append( path )
        else:
            for i in range(len(nums)):
                if target - nums[i] < 0:
                    break
                self.dfs( nums[i+1:], Len, target- nums[i], path + [nums[i]], ans)
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = range(1,10)
        ans = []
        self.dfs(nums, k, n, [], ans)
        return ans