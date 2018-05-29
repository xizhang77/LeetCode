def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    prod = 1;
    indexzero = [];
    for i in range(len(nums)):
        if nums[i] != 0:
            prod = prod * nums[i]
        else:
            indexzero.append(i)
    
    if len(indexzero)>=2:
        ans = [0] * len(nums)
    elif len(indexzero)==1:
        ans = [0] * len(nums)
        ans[indexzero[0]] = prod
    else:
        for i in range(len(nums)):
            ans.append(prod/nums[i])

    return ans


print productExceptSelf([0, 1])