'''
104. Maximum Depth of Binary Tree
Difficulty: Easy
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from 
the root node down to the farthest leaf node.

Example 
Input: root = [3,9,20,null,null,15,7]
Output: 3
'''
# Solution
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # recursive depth-first search
        # T: O(n) visit every node in the tree; 
        # S: O(h), h is the tree height, 
        # recursive call stacks going down to the bottom of the tree
        if not root:
            return 0
        # find the max depth of the left subtree
        left = self.maxDepth(root.left)
        # find the max depth of the right subtree
        right = self.maxDepth(root.right)
        # max. depth = max. depth of subtree + root node
        return 1 + max(left, right)
    
'''
Test Case
root = [3,9,20,null,null,15,7]
Output
3
'''