def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    elements = list(set(nums))
    for i in range(len(elements)):
    	if(nums.count(elements[i])>n/2):
    		ans = elements[i]
    		break
    
    return ans

print majorityElement([])