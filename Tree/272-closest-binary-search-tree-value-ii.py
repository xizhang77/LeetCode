# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution1: Stack
# Time&Space: O(logn)
class Solution(object):
    def getPredecessor(self, nodes):
        curr = nodes.pop()
        node = curr.left 
        while node:
            nodes.append( node )
            node = node.right
        
        return curr.val
            
    def getSuccessor(self, nodes):
        curr = nodes.pop()
        node = curr.right 
        
        while node:
            nodes.append( node )
            node = node.left
        
        return curr.val
        
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        smaller, larger = [], []
        
        while root:
            if root.val <= target:
                smaller.append( root )
                root = root.right
            else:
                larger.append( root )
                root = root.left
        
        ans = []
        for _ in range(k):
            if smaller and (not larger or target - smaller[-1].val <= larger[-1].val - target):
                ans.append( self.getPredecessor(smaller) )
            else:
                ans.append( self.getSuccessor(larger) )
        
        return ans

# Solution2: Priority Queue
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