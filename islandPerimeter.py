'''
LeetCode #463

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). 
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.
'''

class Solution(object):
	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""

		if grid == []:
			return 0

		ans = 0
		num_row = len(grid)
		num_col = len(grid[0])
		print num_row, num_col

		for i in range(num_row):
			for j in range(num_col):
				if grid[i][j] == 1:
					adjacent = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
					for k in adjacent:
						if k[0] < 0 or k[0] == num_row or k[1] < 0 or k[1] == num_col or grid[k[0]][k[1]] == 0 :
							ans += 1

		return ans


obj = Solution()
print obj.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])