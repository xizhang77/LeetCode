# -*- coding: utf-8 -*-

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

# Soluiton 1 [Divide and Conquer, LTE, 199 / 200 test cases passed.]
# Time: O(n^2); Space: O(n)
class Solution(object):
    def profit(self, prices):
        ans = 0
        buy = float('inf')
        for price in prices:
            if price < buy:
                buy = price 
            else:
                temp = price - buy
                ans = max(ans, temp)
        
        return ans
            
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        
        for i in range( len(prices) ):
            temp = self.profit( prices[:i+1] ) + self.profit( prices[i+1:] )
            ans = temp if temp > ans else ans
        
        return ans


# Solution 2 [Modified based on solution 1 ]
# Time & Space: O(n)
# Can be updated later (merge the last 2 for loops)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        leftMax = 0
        left = [ 0 for _ in range(n) ]
        
        buy = float('inf')
        for i in range( n ):
            if prices[i] < buy:
                buy = prices[i] 
            else:
                temp = prices[i] - buy
                leftMax = max(leftMax, temp)
            left[i] = leftMax
            
        rightMax = 0
        right = [ 0 for _ in range(n) ]
        sell = -float('inf')
        
        for i in range( n-1, -1, -1 ):
            if prices[i] > sell:
                sell = prices[i]
            else:
                temp = sell - prices[i]
                rightMax = max(rightMax, temp)
            right[i] = rightMax
        
        right += [0]
        
        ans = 0
        for i in range( n ):
            ans = max( left[i] + right[i + 1], ans )
        return ans