import numpy as np
def transpose(A):
	"""
	:type A: List[List[int]]
	:rtype: List[List[int]]
	"""

	return np.transpose(A).tolist()

print transpose([[1,2,3],[4,5,6]])
        