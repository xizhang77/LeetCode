# -*- coding: utf-8 -*-

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

'''

'''
Refer: https://blog.csdn.net/fuxuemingzhu/article/details/82656899

[真的好难啊…看了很多分析才算勉强理解了…]

'''
# Time & Space: O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        
        buy, sell = [ 0 ] * n, [ 0 ] * n
        buy[ 0 ] = - prices[0]
        
        for i in range( 1, n ):
            if i >= 2:
                buy[ i ] = max( buy[i-1], sell[i-2] - prices[i] )
            else:
                buy[ i ] = max( buy[i-1], - prices[i] )
            
            sell[ i ] = max( sell[i-1], buy[i-1] + prices[i] )
            
        
        return sell[-1]