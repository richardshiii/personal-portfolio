'''
230. Kth Smallest Element in a BST
Difficulty: Medium
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example:
Input: root = [3,1,4,null,2], k = 1
Output: 1
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def kthSmallest(self, root):
        # T: O(k): only need to find the kth element
        # S: O(n): recursive call stack
        # BST inorder traversal to output a sorted list
        # store traversal result in a list
        # since 1-based index, res[k - 1] is the kth smallest value
        self.res = []
        self.count = 0

        def inorder(node):
            if not node:
                return None
            # inorder traversal
            inorder(node.left)
            # store node val in list
            self.count += 1
            if self.count == k:
                self.res = node.val
                return self.res

            inorder(node.right)
        # run helper function and get the value
        inorder(root)
        return self.res
'''
Test Case
root = [3,1,4,null,2]
k = 1
Output
1
'''