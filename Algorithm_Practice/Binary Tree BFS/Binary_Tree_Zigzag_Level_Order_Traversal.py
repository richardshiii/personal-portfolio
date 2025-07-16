'''
103. Binary Tree Zigzag Level Order Traversal
Difficulty: Medium
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
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
    def zigzagLevelOrder(self, root):
        # T: O(n): visit every node 
        # S_queue: O(w): max. width of the tree
        # S_res: O(n): store every node in the result list
        # edge case
        if not root:
            return []
        # initialize the result list
        res = []
        # enqueue the root node
        q = deque([root])
        # start the level order traversal 
        while q:
            # number of nodes in current level & initialize result list for current level
            qlen = len(q)
            level_res = []
            # traverse the current level
            for i in range(qlen):
                # pop node from the left & append result in level_res
                node = q.popleft()
                level_res.append(node.val)
                # enqueue left & right children if exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # append level_res to the main result list
            res.append(level_res)
        # apply zigzag: 
        # reverse element in the result list with odd index
        for i in range(len(res)):
            if i%2 == 1:
                res[i] = res[i][::-1]
        return res
'''
Test Case
root = [3,9,20,null,null,15,7]
Output
[[3],[20,9],[15,7]]
'''