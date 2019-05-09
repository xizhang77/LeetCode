
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1 [Iterative/DFS]. Time: O(n); Space: O(lgn) [bounded by the # of leaves]

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        current = [ root ]
        
        while current:
            value = []
            nextLevel = []
            for node in current:
                if node:
                    value.append( node.val )
                    nextLevel.append( node.left )
                    nextLevel.append( node.right )
                else:
                    value.append( None )
            if value != value[::-1]:
                return False
            current = nextLevel
        
        return True


# Solution 2 [Recursive/BFS]. Time: O(n); 
# Space: O(n) [Bounded by the height of tree. Worst case, the tree is linear and the height is in O(n)]

class Solution(object):
    def dfs(self, node1, node2):
    	if node1 and node2:
        	return (node1.val == node2.val) & self.dfs(node1.right, node2.left) & self.dfs(node1.left, node2.right)
        else:
        	return node1 == node2
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        
        return self.dfs( root, root )
