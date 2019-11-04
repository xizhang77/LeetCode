# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    def dfs(self, root, hashmap, x, y ):
        if not root:
            return
        if x not in hashmap:
            hashmap[ x ] = {}
        if y not in hashmap[ x ]:
            hashmap[ x ][ y ] = [ root.val ]
        else:
            hashmap[ x ][ y ] += [ root.val ]
        
        self.dfs( root.left, hashmap, x - 1 , y - 1 )
        self.dfs( root.right, hashmap, x + 1 , y - 1 )

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        hashmap = {}
        self.dfs( root, hashmap, 0, 0 )
        
        ans = []
        list_x = sorted( hashmap.keys() )
        
        for x in list_x:
            temp = []
            for key in sorted( hashmap[x].keys(), reverse = True ):
                # print hashmap[ x ][ key ]
                temp += sorted( hashmap[x][key] )
            ans.append( temp )
        return ans
        