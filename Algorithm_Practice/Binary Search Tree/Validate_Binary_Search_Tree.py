'''
98. Validate Binary Search Tree
Difficulty: Medium
https://leetcode.com/problems/validate-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBST(self, root):
        # T: O(n): visit each node in the tree once
        # S: O(n): recursive call stack
        # BST: left subtree of a node must be less than the node's value
        # BST: right subtree of a node must be greater then the node's value
        # recursively compare every node and its left and right children
        def validate(node, low = float('-inf'), high = float('inf')):
            # an empty node is valid by default
            if not node:
                return True
            # return false if the tree violates BST rules
            if not (low < node.val < high):
                return False
            # Recursively validate the left and right subtrees:
            # - Left child must be less than current node value, so 'high' becomes node.val
            # - Right child must be greater than current node value, so 'low' becomes node.val
            return validate(node.left, low, node.val) and \
            validate(node.right, node.val, high)
        # start validation from the root node
        return validate(root)
            
'''
Test Case
root = [2,1,3]
Output
True
'''