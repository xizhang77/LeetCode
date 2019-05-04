import math
from collections import Counter
def ifPrime( num ):
	if num == 1:
		return 0
	elif num == 2:
		return 1
	for i in range(2, int(math.sqrt(num))+1 ):
		if num%i == 0:
			return 0
	return 1

def countPrimeSetBits(L, R):
	"""
	:type L: int
	:type R: int
	:rtype: int
	"""
	NumBit = [bin(num).count("1") for num in xrange(L, R+1)]
	BitSet = dict(Counter(NumBit))
	ans = 0
	for num in BitSet.keys():
		if ifPrime( num ):
			ans = ans + BitSet[num]
	return ans


print countPrimeSetBits(6, 10)