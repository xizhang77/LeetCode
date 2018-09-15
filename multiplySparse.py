class Solution(object):
	def multiply(self, A, B):
		"""
		:type A: List[List[int]]
		:type B: List[List[int]]
		:rtype: List[List[int]]
		"""

		rowA = len(A)
		colB = len(B[0])
		colA = len(A[0])

		ans = [[0 for i in range(colB)] for j in range(rowA)]
		
		for i in range(rowA):
			for j in range(colA):
				if A[i][j]:
					for k in range(colB):
						if B[j][k]:
							ans[i][k] += A[i][j]*B[j][k]

		return ans


obj = Solution()
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
print obj.multiply(A, B)