'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	# Insert Node
	def insert(self, data):
		if self.val:
			if data < self.val:
				if self.left is None:
					self.left = TreeNode(data)
				else:
					self.left.insert(data)
			elif data > self.val:
				if self.right is None:
					self.right = TreeNode(data)
				else:
					self.right.insert(data)
		else:
			self.val = data

	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		ans = []
		if root:
			ans = self.inorderTraversal(root.left)
			ans.append(root.val)
			ans = ans + self.inorderTraversal(root.right)
		return ans

class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		ans = []
		if not root:
			return ans
		current_level = [root]
		while current_level:
			next_level = []
			current_ans = []
			for item in current_level:
				current_ans.append(item.val)
				if item.left:
					next_level.append(item.left)
				if item.right:
					next_level.append(ietm.right)
			ans.append(current_ans)
			current_level = next_level
		return ans



tree = TreeNode(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

print tree.inorderTraversal(tree)