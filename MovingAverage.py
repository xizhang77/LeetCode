import collections

class MovingAverage(object):
	def __init__(self, size):
		"""
		Initialize your data structure here.
		:type size: int
		"""
		self.queue = collections.deque(maxlen = size)

	def next(self, val):
		"""
		:type val: int
		:rtype: float
		"""
		self.queue.append(val)
		return float(sum(self.queue))/len(self.queue)


obj = MovingAverage(size)
param_1 = obj.next(val)