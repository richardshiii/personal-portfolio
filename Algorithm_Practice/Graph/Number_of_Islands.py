'''
200. Number of Islands
Difficulty: Medium
https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume 
all four edges of the grid are all surrounded by water.

Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''
# Solution
from collections import deque

class Solution:
    def numIslands(self, grid):
        # T: O(m*n): each cell is visited once
        # S: O(m*n): worst case store each cell in the visit set
        # edge case
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        # island visited, track visited cells to avoid revisiting
        visit = set()
        islands = 0

        def bfs(r, c): # iterative algorithm
            # BFS from the starting cell (r, c)
            q = deque()
            # record row & col of the point visited
            visit.add((r, c)) # mark the starting cell as visited
            q.append((r, c)) # enqueue the starting cell
            # try to expand island when queue is not empty
            # explore the island until there are no more connected land cells
            while q:
                row, col = q.popleft()
                # track the adjacent position
                # 4 directions: right, left, up, down
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # check if the positions are inbound & make sure the position is land
                    # & this position has not been visited
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == "1" and  
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        # visit every position in the grid & find 1s
        # increment island count is that point is not previously visited
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    # use BFS to explore the whole island
                    bfs(r, c)
                    # increment island count
                    islands += 1
        return islands

'''
Test Case

Output

'''