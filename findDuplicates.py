def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums = sorted(nums)
    ans = []
    
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            ans.append(nums[i])
                
    return ans

findDuplicates([2,4,3,4,5,1,2])