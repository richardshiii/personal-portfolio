'''
36. Valid Sudoku
Difficulty: Medium
https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
# Solution
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # T: O(1) the board is fixed at 9*9, and we iterate over each cell only once
        # S: O(1) board size and digits are fixed
        # use hashmap to store unique values in each column, row and 3*3 square
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        # row and col index in squares are row//3 and col//3 -> 9 squares in a 9x9 matrix
        squares = collections.defaultdict(set)

        # traverse the entire 9x9 grid
        for r in range(9):
            for c in range(9):
                # empty space is valid and represented by '.'
                # so when encounter an empty space, continue the loop
                if board[r][c] == '.':
                    continue
                # check if duplicate exists in each row, col and square
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]
                   ):
                   return False
                # if not duplicate, add the value to corresponding hashmap
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        # if no conflicts found after traversing the whole grid, return  true
        return True

'''
Test Case
board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
Output
True
'''