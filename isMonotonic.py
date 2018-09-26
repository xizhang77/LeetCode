'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
'''

class Solution(object):
	def isMonotonic(self, A):
		"""
		:type A: List[int]
		:rtype: bool
		"""
		n = len(A)
		if n <= 1:
			return True
		isInc = all( A[i+1] - A[i] >= 0 for i in range(n-1) )
		isDec = all( A[i+1] - A[i] <= 0 for i in range(n-1) )

		return (isInc or isDec)
		
obj = Solution()
print obj.isMonotonic([1,3,1])
