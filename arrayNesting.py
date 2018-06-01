def arrayNesting(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    for pointer in range(len(nums)):
    	count = 0;
    	while nums[pointer]>=0:
    		prepointer = pointer
    		pointer = nums[pointer]
    		nums[prepointer] = -1
    		count += 1
    	ans = max(ans, count)
    return ans


print arrayNesting([0,3,1,4,2])