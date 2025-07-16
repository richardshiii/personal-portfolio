'''
106. Construct Binary Tree from Inoder and Postorder Traversal
Difficulty: Medium
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150

Given two integer arrays inorder and postorder where inorder is the inorder traversal 
of a binary tree and postorder is the postorder traversal of the same tree, 
construct and return the binary tree.

Example:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        # use hashmap to store node:index pair in the inorder traversal
        # makes root node index search to O(1)
        IndexHash = {v:i for i, v in enumerate(inorder)}
        # if inorder is empty, it is impossible to determine tree structure
        if not inorder:
            return None
        # root node is always the last node in postorder traversal
        root = TreeNode(postorder.pop())
        # find where root node is in the inorder traversal
        # left of root is the left subtree, right of root is the right subtree
        idx = IndexHash[root.val]
        # recursively build the left and right subtree
        # right tree: right of the idx
        # left tree: left of the idx
        root.right = self.buildTree(inorder[idx + 1: ], postorder)
        root.left = self.buildTree(inorder[0:idx], postorder)

        return root
'''
Test Case
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Output
[3,9,20,null,null,15,7]
'''