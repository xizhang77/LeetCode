# -*- coding: utf-8 -*-

'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
'''

'''
注释：最初的想法是存一个[index]*weight[index]的table，然后直接返回table[rand]即可，但对于weight非常大的case会MLE。
    所以需要建立一个cummulate weight sum的数组，然后根据rand的数值，找到所在区间，返回index
'''

class Solution(object):

    def __init__(self):
        self.table= [0]*len(w)
        self.table[0] = w[0]
        for i in range(1, len(w)):
            self.table[i] = self.table[i-1] + w[i]


    def pickIndex(self):
        total = self.table[-1]
        rand = random.randint(0, total - 1)

        start, end = 0, len(self.table) - 1

        while (end - start) > 1:
            if self.table[ (start + end)/2 ] <= rand:
                start = (start + end)/2
            else:
                end = (start + end)/2

        if rand < self.table[start]:
            return start

        return end



#The following solution is Memory Limit Exceeded, 55/57 cases passed #
class Solution_MLE(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.table = []        
        for i in range(len(w)):
            self.table += [i] * w[i] 
        
    def pickIndex(self):
        """
        :rtype: int
        """
        total = len(self.table)
        rnd = random.randint(0, total-1)
        
        return self.table[rnd]
