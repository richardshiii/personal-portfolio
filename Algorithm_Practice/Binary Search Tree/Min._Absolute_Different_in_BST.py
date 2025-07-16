'''
530. Minimum Absolute Difference in BST
Difficulty: Easy
https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a Binary Search Tree (BST), 
return the minimum absolute difference between the values of any two different nodes in the tree.

Example:
Input: root = [4,2,6,1,3]
Output: 1

Binary Search Tree (BST)
 - each node has at most two children;
 - all values in the left subtree are less than the node's value;
 - all values in the right subtree are greater than the node's value;
 - ordering rule holds recursively for every node in the tree;
 - inorder traversal of BST: small -> large
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def getMinimumDifference(self, root):
    # T: O(n) visit every node in the tree
    # S: O(n) recursive call stack
    # inorder traversal: results from smallest to largest
    # use prev & min_diff variables to record previous processed node 
    # and the difference between two nodes
        self.min_diff = float('inf')
        self.prev = None
        # inorder traversal of the tree
        def inorder(root):
            if not root:
                return
            # go left to find the smallest value
            inorder(root.left)
            # if there is a previous value, we are in middle of the traversal
            # and we can find a difference
            if self.prev is not None:
                self.min_diff = min(self.min_diff, root.val - self.prev)
            # update prev to the current node value
            self.prev = root.val
            # search the right subtree
            inorder(root.right)
        # search the input tree
        inorder(root)
        return self.min_diff

'''
Test Case
root = [4,2,6,1,3]
Output
1
'''