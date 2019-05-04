 def intersection(nums1, nums2):
 	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	return [i for i in set(nums1) & set(nums2)]