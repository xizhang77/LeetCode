def missingNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	# return list(set(range(len(nums)+1)) - set(nums))[0]

	nums = sorted(nums) 
	for i in range(len(nums)):
		if nums[i] != i:
			return i
	return len(nums)


print missingNumber([9,6,4,2,3,5,7,0,1])