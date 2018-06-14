import math
def imageSmoother(M):
	"""
	:type M: List[List[int]]
	:rtype: List[List[int]]
	"""
	num_rows = len(M)
	num_cols = len(M[0])
	ans = [[0 for x in range(num_cols)] for y in range(num_rows)]

	for i in range(len(M)):
		for j in range(len(M[i])):
			count = 0
			summation = 0
			for x in range(max(0, i-1), min(i+2, len(M))):
				for y in range(max(0, j-1), min(j+2, len(M[i]))):
					summation += M[x][y]
					count += 1
			ans[i][j] = summation/count
	return ans

print imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])