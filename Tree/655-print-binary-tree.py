# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/print-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# Time: O(n) where n is number of node
class Solution(object):
    def dfs(self, root, level):
        if not root:
            return [ [ "" ] ]
        
        if level < self.dp:
            left = self.dfs( root.left, level + 1 )
            right = self.dfs( root.right, level + 1 )
        else:
            return [ [str(root.val)] ]
        
        ans = [ [""]*(2**(self.dp-level)-1) + [str(root.val)] + [""]*(2**(self.dp-level)-1)  ]
        
        # print ans, left, right
        
        if len(left) == len(right):
            for i in range( len(left) ):
                
                ans.append( left[i] + [""] + right[i] )
        elif len(left) > len(right):
            for i in range( len(left) ):
                if i < len(right) and right[i] != [""]*len(right[i]):
                    ans.append( left[i] + [""] + right[i] )
                else:
                    ans.append( left[i] + [""]*(len(left[i]) + 1) )
        else:
            for i in range( len(right) ):
                if i < len(left) and left[i] != [""]*len(left[i]):
                    ans.append( left[i] + [""] + right[i] )
                else:
                    ans.append( [""]*(len(right[i]) + 1) + right[i] )
        
        return ans
    
    
    def depth(self, root, level):
        if not root:
            return
        self.dp = max(self.dp, level)
        self.depth( root.left, level + 1 )
        self.depth( root.right, level + 1 )
        
        
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        self.dp = 0
        self.depth( root, 1 )
                
        return self.dfs( root, 1 )