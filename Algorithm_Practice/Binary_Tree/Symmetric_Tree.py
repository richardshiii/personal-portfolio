'''
101. Symmetric Tree
Difficulty: Easy
https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Example:
Input: root = [1,2,2,3,4,4,3]
Output: true
'''
# Solution
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode] 
        :rtype: bool
        """
        # T: O(n): visit each node once
        # S: O(h): call stack of tree height
        # helper function to recursively check if two subtrees are mirror images
        def sym(root1, root2):
            # return true if neigher tree exists
            if not root1 and not root2:
                return True
            # return false if only one tree exists
            if not root1 or not root2:
                return False
            # both nodes exist but with different values -> asymmetric
            if root1.val != root2.val:
                return False
            # recursive case:
            # the left subtree must be a mirror of the right subtree, vice versa
            return sym(root1.left, root2.right) and \
                    sym(root1.right, root2.left)
        # start with the root node, compare itself
        return sym(root, root)
             
'''
Test Case

Output

'''