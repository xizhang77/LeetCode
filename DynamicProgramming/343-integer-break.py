# -*- coding: utf-8 -*-

'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Note: You may assume that n is not less than 2 and not larger than 58.

'''
# Solution 1: DP
# Time: O(n^2); Space: O(n)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1, 1]
        
        for num in range(3, n+2):
            i, j = 0, len(ans) - 1
            temp = num - 1
            while i <= j:
                temp = max( temp, ans[i]*ans[j], (i+1)*(j+1), (i+1)*ans[j], (j+1)*ans[i] )
                i += 1
                j -= 1
            ans.append(temp)

        return ans[n-1]

# Solution 2: Math & Recursive
# Time & Space: at most O(n)