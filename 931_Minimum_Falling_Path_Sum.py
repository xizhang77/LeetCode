class Solution(object):
    def dfs(self, A, i, path, n):
        if len(path) == n:
            self.ans = sum(path) if sum(path) < self.ans else self.ans
            return
        nums = A[0]
        direct = [-1, 0, 1]
        for j in range(len(direct)):
            ii = i + direct[j]
            if ii >= 0 and ii < n:
                self.dfs(A[1:], ii, path + [nums[ii]], n )
            
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        
        self.ans = float('inf')
        
        for i in range(n):
            self.dfs( A[1:], i, [A[0][i]], n)
        
        return self.ans