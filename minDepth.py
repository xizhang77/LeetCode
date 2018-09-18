'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		if not root:
			return 0

		depth = 1
		current_level = [root]

		while current_level:
			next_level = []
			for item in current_level:
				if not item.left and not item.right:
					return depth
				if item.left:
					next_level.append(item.left)
				if item.right:
					next_level.append(item.right)
			current_level = next_level
			depth += 1



        