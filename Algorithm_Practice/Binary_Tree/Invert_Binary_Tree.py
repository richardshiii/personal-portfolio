'''
226. Invert Binary Tree
Difficulty: Easy
https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, invert the tree, and return its root.

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
'''
# Solution
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # T: O(n): visit every node in the tree
        # S: O(h): call stack of height of the tree (h)
        # deal with edge case: tree does not exist
        if not root:
            return None
        # swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        # recursively call the function on the left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root        
'''
Test Case
root = [2,1,3]
Output
[2,3,1]
'''