# -*- coding: utf-8 -*-

'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
        	return ans

        table = {}
        curr_level = [[root, 0]]

        while curr_level:
        	next_level = []
        	for node in curr_level:
        		if node[1] not in table:
        			table[node[1]] = node[0].val
        		else:
        			table[node[1]].append(node[0].val)

        		if node[0].left:
        			next_level.append([node[0].left, node[1] - 1])
        		if node[0].right:
        			next_level.append([node[0].right, node[1] + 1])
        	next_level = curr_level

        for val in sorted(table):
        		ans.append( table[val] )
        
        return ans
