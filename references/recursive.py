import math
import numpy as np

test = np.array([(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,19),(7,29),(10,11),(1,13)])

def bruteforce (cooridnates):
	n = cooridnates.shape[0]
	all_pairs = []
	print type(all_pairs)
	for i in range(0, n):
		for j in range(i+1, n):
			x = cooridnates[i, :]
			y = cooridnates[j, :]
			dist = np.linalg.norm(x-y)
#            dist = math.sqrt((xi-xj)**2 + (yi-yj)**2)
			all_pairs = np.append( all_pairs, dist)

	return min(all_pairs)

bruteforce(test)
    




