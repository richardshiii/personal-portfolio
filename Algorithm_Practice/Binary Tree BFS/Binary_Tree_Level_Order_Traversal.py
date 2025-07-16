'''
102. Binary Tree Level Order Traversal
Difficulty: Medium
https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root):
        # T: O(n): visit every node in the tree
        # S: O(w): maximum width possible of the tree
        # edge case
        if not root:
            return []
        # use list to store results
        # enqueue the root node
        res = []
        que = deque([root])
        # BFS traversal level by level
        while que:
            # number of nodes in the current level
            qlen = len(que)
            # record results in the current level
            level_res = []
            # iterate through each node in the current level
            for i in range(qlen):
                # pop the node from left & append its value to the list
                node = que.popleft()
                level_res.append(node.val)
                # enqueue left & right node if exist
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            # append results of each level 
            res.append(level_res)
        
        return res
  
'''
Test Case
root = [3,9,20,null,null,15,7]
Output
[[3],[9,20],[15,7]]
'''