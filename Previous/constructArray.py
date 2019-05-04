def constructArray(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[int]
    """
    wholeset = range(1, n+1)
    ans = []
    for i in range(1,k+1):
        if i%2:
            ans.append(wholeset.pop(0))
        else:
            ans.append(wholeset.pop(-1))
    if k%2:
        ans = ans + wholeset
    else:
        ans = ans + wholeset[::-1]

    return ans



print constructArray(10, 5)