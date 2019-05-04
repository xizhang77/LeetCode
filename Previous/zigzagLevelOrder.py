'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		ans = []
		if not root:
			return ans
		mark = 1
		current_level = [root]
		while current_level:
			current_ans = []
			next_level = []
			for item in current_level:
				current_ans.append(item.val)
				if item.left:
					next_level.append(item.left)
				if item.right:
					next_level.append(item.right)
			if mark:
				ans.append(current_ans)
			else:
				ans.append(list(reversed(current_ans)))
			current_level = next_level
			mark = 1 - mark

		return ans

		