'''
130. Surrounded Regions
Difficulty: Medium
https://leetcode.com/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150

You are given an m x n matrix board containing letters 'X' and 'O', 
capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells 
if you can connect the region with 'X' cells and 
none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with '
X's in-place within the original board. You do not need to return anything.

Example:
Input: board = 
[["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"]]

Output: 
[["X","X","X","X"],
["X","X","X","X"],
["X","X","X","X"],
["X","O","X","X"]]
'''
# Solution
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # T: O(m*n): each cell is visited once at most
        # S: O(m*n): space needed for recursion stack if all cells are "O"
        rows, cols = len(board), len(board[0])
        
        def capture(r, c):
            # check if out of bounds or not "O"
            if (r < 0 or c < 0 or r == rows or c == cols 
                or board[r][c] != "O"):
                return 
            # temporarily mark "O" as "T" to indicate it's connected to border
            board[r][c] = "T"
            # DFS four adjacent directions
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        # 1. Capture unsurrounded regions (all regions connected to the border) O -> T; DFS
        # border "O"s and cells connected to them
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1])):
                    capture(r, c)
        # 2. Capture surrounded regions (O -> X); Nested for-loop
        # unmarked "O"s to "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # 3. Uncapture unsurrounded regions (T -> O) for-loop
        # marked "T"s back to "O"s
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
'''
Test Case
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
'''