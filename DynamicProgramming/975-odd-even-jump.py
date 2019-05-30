# -*- coding: utf-8 -*-
'''
https://leetcode.com/problems/odd-even-jump/
'''

# Solution 1: LTE.....
# Time: O(n^2); Space: O(n)
'''
根据参考答案，这道题主要的问题在于查找（solution中第一个for循环），压缩时间复杂度的方法是使用TreeMap
可以将complexity从 O(n^2) 压缩到 O(nlgn)。但是python中没有定义好的TreeMap...
'''
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        n = len(A)
        
        idx = [ [ -1 ]* n for _ in range(2) ]
        
        for i in range( n - 1 ):
            oddIdx, oddVal = -1, float('inf')
            evenIdx, evenVal = -1, - float('inf')
            for j in range( i + 1, n ):
                if A[i] <= A[j] and A[j] < oddVal:
                    oddIdx, oddVal = j, A[j]
                if A[i] >= A[j] and A[j] > evenVal:
                    evenIdx, evenVal = j, A[j]
            idx[0][i], idx[1][i] = evenIdx, oddIdx
        
        dp = [ False ] * n
        
        for i in range( n ):
            path = []
            step = 0
            p = i
            while p != -1 and p != n - 1:
                step += 1
                path += [ i ]
                if dp[ p ]:
                    p = n - 1
                    break
                p = idx[ step%2 ][ p ]
            if p == n - 1:
                for j in path:
                    dp[ j ] = True
                count += 1
        
        return count


# Solution 2: Stack + DP
# Refer: https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-idea-Using-TreeMap-or-Stack
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        
        next_low, next_high = [ 0 ] * n, [ 0 ] * n
        
        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_high[ stack.pop() ] = i
            stack.append( i )
        
        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_low[ stack.pop() ] = i
            stack.append( i )
                
        lower, higher = [ 0 ] * n, [ 0 ] * n
        lower[-1] = higher[-1] = 1
        for i in range( n - 2, -1, -1 ):
            higher[ i ] = lower[ next_high[i] ]
            lower[ i ] = higher[ next_low[i] ]
        
        return sum( higher )