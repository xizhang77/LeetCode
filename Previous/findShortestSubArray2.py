def findShortestSubArray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	# elements = list(set(nums))
	# count = [nums.count(x) for x in elements]
	# mydict = dict(zip(elements, count))
	mydict = dict()

	for i in range(len(nums)):
		if nums[i] in mydict:
			mydict[nums[i]].append(i)
		else:
			mydict[nums[i]] = [i]

	count = [len(mydict[x]) for x in mydict.keys()]
	degree = max(count)


	ans = min(mydict[x][-1]-mydict[x][0] + 1 for x in mydict.keys() if len(mydict[x])==degree)
	print ans


print findShortestSubArray([1,2,2,3,1,4,2])