def findPoisonedDuration(timeSeries, duration):
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    ans = 0

    for i in range(len(timeSeries)-1):
        if timeSeries[i+1] - timeSeries[i] > duration:
            ans = ans + duration
        else:
            ans = ans + timeSeries[i+1] - timeSeries[i]
    if len(timeSeries)!=0:
        ans = ans + duration

    return ans

print findPoisonedDuration([1,3,7,8], 3)