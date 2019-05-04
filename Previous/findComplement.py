def findComplement(num):
	"""
	:type num: int
	:rtype: int
	"""
	CheckPos = False

	for i in range(31, -1, -1):
		if num&(1<<i):
			CheckPos = True
		if CheckPos:
			mask = (1<<(i+1)) - 1 
			print mask
			return num^mask

	#print bin(num)
	#print bin(~num)
	#print num, ~num
	#print ~num & 0xF
	#print num ^ 0xF


print findComplement(1)