# -*- coding: utf-8 -*-
'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

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

class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""

		numCoin = len(coins)

		dp = [ [0 for i in range(amount + 1)] for j in range(numCoin + 1)]
		print len(dp), len(dp[0])

		for j in range(amount + 1):
			dp[0][j] = float('inf')

		for i in range(numCoin):
			dp[i][0] = 0

		print dp

		for i in range(1, numCoin + 1):
			for j in range(1, amount + 1):
				if j < coins[i - 1]:
					temp = float('inf')
				else:
					temp = dp[i][j - coins[i - 1]] + 1

				dp[i][j] = min(dp[i-1][j], temp)

		print dp

		return dp[numCoin][amount] if dp[numCoin][amount] != float('inf') else -1

obj = Solution()
print obj.coinChange( [1,2,5], 11 )

'''
A more simplified and faster version.
'''
class BetterSolution(object):
	def coinChange(self, coins, amount):

		MAX = float('inf')
		dp = [0] + [MAX] * amount
		for i in range(1, amount + 1):
			dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

		print dp[amount] if dp[amount] != MAX else -1

obj2 = BetterSolution()
print obj2.coinChange( [1,2,5], 11 )

