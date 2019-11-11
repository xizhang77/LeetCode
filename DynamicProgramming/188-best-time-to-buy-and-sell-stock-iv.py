# -*- coding: utf-8 -*-

'''
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

# Reference: https://blog.csdn.net/u013383813/article/details/84882867
# local[i][j]: the profit of finish j-th transaction at i-th day
# glob[i][j]: the profit at i-th day (j trans finished, may or may not have trans at i-th day)
# Time: O(nk); Space: O(nk)
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k <= 0 or not prices:
            return 0
        
        n = len(prices)
        
        if k >= n:
            ans = 0
            buy = prices[0]
            for val in prices[1:]:
                if val > buy:
                    ans += val - buy
                buy = val
            return ans
    
        local = [ [0]*(k+1) for _ in range( n ) ]
        glob = [ [0]*(k+1) for _ in range( n ) ]
        
        for i in range( 1, n ):
            diff = prices[i] - prices[i-1]
            for j in range( 1, k+1 ):
                local[i][j] = max( glob[i-1][j-1] + max(diff, 0), local[i-1][j] + diff )
                glob[i][j] = max( glob[i-1][j], local[i][j] )
        
        return glob[-1][-1]