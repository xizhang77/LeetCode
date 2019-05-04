class Solution(object):
	def multiply(self, A, B):
		"""
		:type A: List[List[int]]
		:type B: List[List[int]]
		:rtype: List[List[int]]
		"""

		m = len(A)
		n = len(B[0])
		l = len(A[0]) # Shared index

		ans = [[0 for i in range(n)] for j in range(m)]
		
		for i in range(m):
			for k in range(l):
				if A[i][k]:
					for j in range(n):
						if B[k][j]:
							ans[i][j] += A[i][k]*B[k][j]

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