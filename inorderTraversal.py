'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
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


class Solution(object):
	# Inorder: Left -> Root -> Rights
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



tree = TreeNode(1)
tree.insert(None)
tree.insert(2)
tree.insert(3)

obj = Solution()
print obj.inorderTraversal(tree)