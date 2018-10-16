def merge(nums1, m, nums2, n):
	"""
	:type nums1: List[int]
	:type m: int
	:type nums2: List[int]
	:type n: int
	:rtype: void Do not return anything, modify nums1 in-place instead.
	"""
	i = 0
	j = 0
	while i<m and j<n:
		if nums1[i] < nums2[j]:
			i = i + 1
		else:
			nums1.insert(i, nums2[j])
			j = j + 1
			i = i + 1
	
	if j>=n:
		return nums1[:m+n]
	else:
		return nums1[:m+j] + nums2[j:]


print merge([1,2,3,0,0,0], 3, [2,5,6], 3)