def twoSum(numbers, target):
	"""
	:type numbers: List[int]
	:type target: int
	:rtype: List[int]
	"""
	n = len(numbers)
	left = 0
	right = n-1
	while 1:
		if numbers[left] + numbers[right] < target :
			left += 1
		elif numbers[left] + numbers[right] > target:
			right -= 1
		else:
			return [left+1, right+1]
			break


print twoSum([2,7,11,15], 18)