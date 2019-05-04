def largeGroupPositions(S):
	"""
	:type S: str
	:rtype: List[List[int]]
	"""
	ans = []
	n = len(S)
	pointer = 0
	while pointer<n-1:
		end = pointer+1
		while end<n and S[end]==S[pointer]:
			end += 1
		if end-pointer>=3:
			ans.append([pointer, end-1])
		pointer = end
	return ans


print largeGroupPositions("abbxxxxzyy")