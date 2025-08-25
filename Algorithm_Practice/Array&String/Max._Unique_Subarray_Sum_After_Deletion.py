'''
3487. Maximum Unique Subarray Sum After Deletion
Difficulty: Easy
https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=daily-question&envId=2025-07-25

You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. 
After performing the deletions, select a subarray of nums such that:
All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.

Example:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation:
Select the entire array without deleting any element to obtain the maximum sum.
'''
# Solution
class Solution(object):
    def maxSum(self, nums):
        # T: O(n): worst case iterate through each input number
        # S: O(n): worst case store each input number in the hashset

        # use a set since set only stores unique values
        # only interested in positive numbers since we want to maximize the sum 
        positiveNumSet = set({n for n in nums if n > 0})
        # if the set is empty, meaning there is no positive number in the input,
        # just return the maximum element in the original input
        if len(positiveNumSet) == 0:
            return max(nums)
        # otherwise, return the sum of all recorded unique positive number
        else: 
            return sum(positiveNumSet)
'''
Test Case
nums = [1,1,0,1,1]
Output
1
'''