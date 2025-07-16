'''
100. Same Tree
Difficulty: Easy
https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example:
Input: p = [1,2,3], q = [1,2,3]
Output: true
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p, q):
        # DFS & Recursive programming
        # T: O(n): visit all nodes in both trees
        # S: O(h): recursion stack, height of the tree
        # edge case 1: neither tree exists -> return True
        if not p and not q:
            return True
        # edge case 2: only one tree exists -> return False
        if not p or not q:
            return False
        # edge case 3: both trees exist but values differ -> return False
        if p.val != q.val:
            return False
        # recursive case:
        # check if left subtrees are the same AND right subtrees are the same 
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
    
'''
Test Case
p = [1,2,3]
q = [1,2,3]
Output
True
'''