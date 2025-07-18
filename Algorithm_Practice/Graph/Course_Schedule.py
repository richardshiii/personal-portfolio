'''
207. Course Shedule
Difficulty: Medium
https://leetcode.com/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150

There are a total of numCourses courses you have to take, 
labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
'''
# Solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        # T: O(n + E) go through every node and its edge
        # S: O(n + E) dfs through all nodes + edges of the graph
        from collections import defaultdict
        # build adjacency list to represent a graph
        # key: a course; value: list of prerequisite courses
        graph = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            graph[a].append(b)
        # 3 states: unvisited, in current DFS path, fully explored
        unvisited = 0
        visiting = 1
        visited = 2
        # initialize all courses as unvisited
        states = [unvisited] * numCourses
        # use dfs to check for cycle in the graph
        def dfs(node):
            state = states[node]
            if state == visited:
                # if visited and no cycle detected
                return True
            elif state == visiting:
                # detected a back edge -> cycle exists
                return False
            else:
                # mark node as visiting
                states[node] = visiting
            # traverse all prerequisites of the course
            for nei in graph[node]:
                # if any neighbot causes cycle, return False
                if not dfs(nei): 
                    return False
            # After all neighbors are processed with no cycle, 
            # mark as visited return True
            states[node] = visited
            return True
        # apply DFS to each course
        for i in range(numCourses):
            # If any DFS traversal detects a cycle, return False 
            if not dfs(i):
                return False
        # No cycles detected in any DFS traversal → All courses can be finished
        return True
'''
Test Case
numCourses = 2
prerequisites = [[1,0]]
Output
True
'''