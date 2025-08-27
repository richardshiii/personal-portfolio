'''
977. Squares of a Sorted Array
Difficulty: Easy
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]
'''
# Solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two-pointer solution
        # T: O(n): iterate through the input array once
        # S: O(1): if the output array does not count as extra space
        # create the result array
        res = [1] * len(nums)
        # set up twp pointers
        l = 0
        r = len(nums) - 1
        # iterate through the input array from the end backwards
        for i in range(len(nums)-1, -1, -1):
            # compare the abs. value of the pointed values
            # square the larger value and put it in the result array at position i
            # move the pointer accordingly
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1

        return res

'''
Test Case
nums = [-7, -3, 2, 3, 11]
Output
[4, 9, 9, 49, 121]
'''