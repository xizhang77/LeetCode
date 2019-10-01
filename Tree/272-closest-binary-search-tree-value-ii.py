# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(nlogk); Space: O(k)
import heapq
class Solution2(object):
    def dfs(self, root, target, k, stack):
        if not root:
            return
        if len(stack) < k:
            heapq.heappush( stack, (-abs(root.val-target), root.val) )
            self.dfs( root.left, target, k, stack )
            self.dfs( root.right, target, k, stack )
        else:
            currmax = stack[0][0]
            if abs(root.val-target) < - currmax:
                heapq.heappop( stack )
                heapq.heappush( stack, (-abs(root.val-target), root.val) )
                self.dfs( root.left, target, k, stack )
                self.dfs( root.right, target, k, stack )
            else:
                if root.val < target:
                    self.dfs( root.right, target, k, stack )
                else:
                    self.dfs( root.left, target, k, stack )
        
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        stack = []
        
        self.dfs( root, target, k, stack )
        
        ans = [ val[1] for val in stack ]
        
        return ans