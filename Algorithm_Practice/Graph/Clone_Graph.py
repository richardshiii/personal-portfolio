'''
133. Clone Graph
Difficulty: Medium
https://leetcode.com/problems/clone-graph/?envType=study-plan-v2&envId=top-interview-150

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}

Example:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
'''
# Solution
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node):
        # T: O(n): n=number of edges + number of vertices
        # S: O(1): modified in-place
        # use dictionary to track original node and its clone
        oldToNew = {}

        def dfs(node):
            # edge case
            if not node:
                return None
            # if node already copied: return its clone to prevent cycles
            if node in oldToNew: 
                return oldToNew[node] 
            # if clone does not exist
            # create a new node with the same value & map it to the old node
            copy = Node(node.val)
            oldToNew[node] = copy
            # make copy of each neighbor 
            # recursively clone all neighbors and append them to the current node's copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
'''
Test Case
edges = [[2,4],[1,3],[2,4],[1,3]]
Output
[[2,4],[1,3],[2,4],[1,3]]
'''