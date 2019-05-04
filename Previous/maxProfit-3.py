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

'''
这道题是由maxProfit-1演变而来的，原来是只能有一次，现在是可以有两次，这里有要求是说你不能买一次再买一次然后卖出去两次，只能买卖买卖。
可以考虑将天数分开，前i天调用一次maxProfit-1的算法，后面的天调用一次maxProfit-1的算法。

但是要注意如果外层循环i，里面再循环maxProfit-1的算法，会超时，这时我们考虑用两个数组来存储结果，pre_profit和pro_profit，
其中pre_profit[i]表示i天之前的最大利润，pro_profit[i]表示i天之后的最大利润，
前i天的和maxProfit-1一样的写法，后i天从后往前动态规划。
'''

class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		n = len(prices)
		if n <= 1:
			return 0

		pre_profit = [0] * n

		# Below is the exact solution for maxProfit-1.py (LeetCode #121)
		pre_buy = prices[0]
		for i in range(1, n):
			pre_buy = min(pre_buy, prices[i])
			pre_profit[i] = max( pre_profit[i-1], prices[i] - pre_buy)

		pro_profit = [0] * n

		pro_sell = prices[n-1]
		for i in range(n-2, -1, -1):
			pro_sell = max( pro_sell, prices[i])
			pro_profit[i] = max( pro_profit[i+1], pro_sell - prices[i])
		

		return max( [pre_profit[i] + pro_profit[i] for i in range(n)] )


obj = Solution()
print obj.maxProfit([3,3,5,0,0,3,1,4])
print obj.maxProfit([1,2,3,4,5])



