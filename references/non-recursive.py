import math
import numpy as np

test=[(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,19),(7,29),(10,11),(1,13)]


def bruteforce (n):
    all_pairs=[]
    for i in range (0,n):
        for j in range (1, n):
            x = cooridnates[i:x]
            y = cooridnates[j:x]
            dist = np.linalg.norm(x-y)
#            dist = math.sqrt((xi-xj)**2 + (yi-yj)**2)
            all_pairs=all_pairs.append(dist)
    return min(all_pairs)




