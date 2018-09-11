import collections

def intersect(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""

	set1 = collections.Counter(nums1)
	set2 = collections.Counter(nums2)

	uniqintsect = [i for i in set(nums1) & set(nums2)]
	result = []
	for nums in uniqintsect:
		result.append([nums]*(set1[nums] if set1[nums] < set2[nums] else set2[nums]))

	return sum(result, [])

print intersect([1,2,2,1], [2,2])