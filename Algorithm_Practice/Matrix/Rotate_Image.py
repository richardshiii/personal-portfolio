'''
48. Rotate Image
Difficulty: Medium
https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150

You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''
# Solution
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # T: O(n^2) n*n matrix
        # S: O(1) rotate in-place, no extra space is needed
        # left wall starts at 0, right wall starts at the rightmost position
        left, right = 0, len(matrix) - 1
        # Traverse each layer from outside to inside
        while left < right:
            for i in range(right - left):
                top, bottom = left, right # square matrix
                # rotate in reverse order so only 1 temp. variable needed
                # after one rotation, move pointer by i to start rotation of the next value 
                # save the top left value into a temporary variable
                topLeft = matrix[top][left + i]
                # move the bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]
                # move the bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # move the top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                # move temp. variable into top right
                matrix[top + i][right] = topLeft

            # after rotation of a layer, update pointers to move to the inner layer
            right -= 1
            left += 1

'''
Test Case
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output
[[7,4,1],[8,5,2],[9,6,3]]
'''