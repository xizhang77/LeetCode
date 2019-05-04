def findShortestSubArray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	elements = list(set(nums))
	count = [nums.count(x) for x in elements]
	mydict = {elements[i]: [count[i], 0, 0, 0] for i in range(len(elements))}

	for i in range(len(nums)):
		if mydict[nums[i]][1] == 0:
			mydict[nums[i]][1] += 1
			mydict[nums[i]][2] = i
		else:
			mydict[nums[i]][1] += 1

		if mydict[nums[i]][1] == mydict[nums[i]][0]:
			mydict[nums[i]][3] = i

	# print mydict

	maxcount = max(count)
	ans = len(nums)
	for j in mydict:
		if mydict[j][0] == maxcount:
			sublen = mydict[j][3] - mydict[j][2] + 1
			if sublen<=ans:
				ans = sublen

	return ans

print findShortestSubArray([2, 2])