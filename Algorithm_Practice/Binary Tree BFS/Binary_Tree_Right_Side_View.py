'''
199. Binary Tree Right Side View
Difficulty: Medium
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
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
    def rightSideView(self, root):
        # T: O(n): visit every node once
        # S: O(w): w is the largest possible size of the queue(tree width)
        res = []
        # initialize queue for BFS with root node
        que = deque([root]) 
        # iterate through each level of the tree & find the rightmost node
        # only pop if queue is not empty
        # level-order traversal
        while que:
            rightside = None
            # number of nodes in the current level
            qlen = len(que)
            # iterate through curren level
            for i in range(qlen): 
                # pop from the left, add from the right
                node = que.popleft()
                if node:
                    # update rightside to the current node; 
                    # the last node processed in the level will be the rightmost
                    rightside = node
                    # enqueue left and right children (if any) for next level
                    que.append(node.left) 
                    que.append(node.right)
            # after the level ends, append the last seen node (rightmost) to result
            if rightside:
                res.append(rightside.val)
        
        return res
        
'''
Test Case
root = [1,2,3,null,5,null,4]
Output
[1,3,4]
'''