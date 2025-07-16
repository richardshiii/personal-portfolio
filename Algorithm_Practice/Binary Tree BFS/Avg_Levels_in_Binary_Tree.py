'''
637. Average of Levels in Binary Tree
Difficulty: Easy
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root):
        # T: O(n): visit every node once
        # S: O(w): w is the largest possible size of the queue(tree width)
        # use BFS to traverse the tree level by level 
        res = []
        # initiate queue with root node for level order traversal
        q = deque([root])
        # traverse through each level
        while q:
            # initialize sum of values at this level
            level_sum = 0
            # number of nodes at this level
            qlen = len(q)
            # iterate through all nodes at this level
            for i in range(qlen):
                # pop node from the front of the queue
                node = q.popleft()
                # add the node's value to avg
                level_sum += node.val
                # enqueue left and right children if exist -> next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # computer avg. by dividing the level_sum by number of nodes
            avg = level_sum / qlen
            # append the result
            res.append(avg)
        
        return res
'''
Test Case
root = [3,9,20,null,null,15,7]
Output
[3.00000,14.50000,11.00000]
'''