'''
54. Spiral Matrix
Difficulty: Medium
https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150

Given an m x n matrix, return all elements of the matrix in spiral order.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''
# Solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #T: O(m*n) traverse the entire input matrix
        #S: O(1) no extra space is needed
        if not matrix:
            return None

        res = []
        left, right = 0, len(matrix[0]) # len(matrix[0]) is col count of the matrix
        top, bottom = 0, len(matrix) # len(matrix) is row count of the matrix

        while left < right and top < bottom:
            # get every value in top row (left to right)
            for i in range(left, right):
                res.append(matrix[top][i])
            # move top wall downward afterwards
            top += 1
            # get every value in the right column (top to bottom)
            for i in range(top, bottom):
                # initially right and bottom wall are just outside the matrix
                res.append(matrix[i][right - 1]) 
            # move right wall leftward
            right -= 1

            # deal with edge cases of 1row or 1col matrix
            if not (left < right and top < bottom):
                break

            # get every value in the bottom row (right to left)
            for i in range(right - 1, left - 1, -1): # -1 is the direction
                res.append(matrix[bottom - 1][i])
            # move bottom wall upward
            bottom -= 1
            # get every value in the left column (bottom to top)
            for i in range(bottom - 1, top - 1, -1): # -1 is the direction
                res.append(matrix[i][left])
            # move left wall rightward
            left += 1

        return res

'''
Test Case
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output
[1,2,3,6,9,8,7,4,5]
'''