def hasAlternatingBits(n):
	"""
	:type n: int
	:rtype: bool
	"""
	mask = n&1
	while ( mask == n&1 ):
		mask = mask^1
		n = n>>1
	return n==0



print hasAlternatingBits(7)