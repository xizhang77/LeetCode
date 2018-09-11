def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	profit = 0
	buy = 0
	for sell in range(1, len(prices)):
		if prices[sell] - prices[buy] < 0:
			buy = sell
		else:
			profit = max( prices[sell] - prices[buy], profit)

	return profit


print maxProfit([7,6,4,3,1])

