'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
'''
# Solution
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # preorder: 1st value is the root node, root -> left -> right
        # inorder: left -> root -> right
        # if either list is empty, there is no tree to construct
        if not preorder or not inorder:
            return None
        # 1st element in preorder traversal is always the root node
        root =  TreeNode(preorder[0])
        # find the index of the root node in the inorder traversal 
        # everything to the left is the left subtree
        # everything to the right is the right subtree
        mid = inorder.index(preorder[0])
        # recursively build the left and right subtree
        # left subtree
        # preorder: skip 1st element, take the next 'mid' element 
        # inorder: elements before 'mid' is the left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        # right subtree
        # preorder: skip root node the left subtree
        # inorder: elements after the root
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1: ])

        return root  
          
'''
Test Case
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Output
[3,9,20,null,null,15,7]
'''