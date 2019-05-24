# -*- coding: utf-8 -*-

'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

'''
# m: len of coins; n: amount
# Time: O(m*n); Space: O(n)

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [ -1 ] * (amount + 1)
        
        dp[0] = 0
        
        for num in range(1, amount + 1):
            temp = float('inf')
            for coin in coins:
                if num - coin >= 0 and dp[ num - coin ] != -1:
                    temp = min( dp[ num - coin ] + 1, temp )
            if temp != float('inf'):
                dp[ num ] = temp
        
        return dp[-1]