'''
108. Convert Sorted Array to Binary Search tree
Difficulty: Easy
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

height-balanced BST: 
a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        # T: O(n): visit each node once
        # S: O(logn): recursive call stack of height of balanced BST
        def helper(l, r):
            # if left index cross right index, return false
            if l > r:
                return None
            # find the mid point in nums & use this value as the root node
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            # recursive programming to look at subtree left to the root node
            root.left = helper(l, mid - 1)
            # recursive programming to look at subtree right to the root node
            root.right = helper(mid + 1, r)

            return root
        # 0, len(nums) - 1 are l & r pointers of the input array
        return helper(0, len(nums) - 1)
        
'''
Test Case
nums = [-10,-3,0,5,9]
Output
[0,-10,5,null,-3,null,9]
'''