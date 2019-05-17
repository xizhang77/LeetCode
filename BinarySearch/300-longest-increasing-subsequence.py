# -*- coding: utf-8 -*-

'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

'''

# Solution 1: DP
# Time: O(n^2); Space: O(2*n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        ans = 0
        for num in nums:
            count = 0
            for i in range( len(dp)-1, -1, -1):
                temp_v, temp_c = dp[i]
                count = temp_c if (temp_c > count and temp_v < num) else count
            dp.append( [num, count + 1 ] )
            ans = count + 1 if count + 1 > ans else ans
            
        return ans

# Solution 2: Binary Search
# Time: O(nlgn); Space: O(n)

'''
基本思想：

维护一个数组A

如果当前数num比数组A最后一个元素大，那么依旧构成一个上升序列，将其放到数组A最后。
否则，二分查找数组A中第一个比num大的数，用num替换之
最后数组A长度即为该未排序数组的最大上升子序列长度 

但要注意该数组并不一定是最大上升子序列（只是长度保持一致）
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        
        for num in nums:
            if not stack or stack[-1] < num:
                ans += 1
                stack.append( num )
                continue
            
            i, j = 0, ans - 1
            while i < j:
                mid = (i + j)/2
                if stack[ mid ] < num:
                    i = mid + 1
                else:
                    j = mid
            stack[j] = num
        
        return ans
