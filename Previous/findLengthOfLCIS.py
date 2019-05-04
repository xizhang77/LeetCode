def findLengthOfLCIS(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""

	if not nums:
		return 0
	if len(nums) == 1:
		return 1

	result = 1
	count = 1

	for i in range(len(nums)-1):
		if nums[i] < nums[i+1]:
			count += 1
		else:
			result = max(result, count)
			count = 1

	return max(result, count)


print findLengthOfLCIS([1,3,5,7])