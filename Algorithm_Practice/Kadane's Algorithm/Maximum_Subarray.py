'''
53. Maximum Subarray
Difficulty: Medium
https://leetcode.com/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Kadane's algorithm
 - efficient method to solve the maximum subarray sum problem
 - at each index, either start a new subarray at current element, 
   or extend the previous subarray
 - current_max = max(current_element, current_element + previous_max) 
'''
# Solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # T: O(n) iterate through the input array
        # S: O(1) no extra memory needed
        # initialize the maxSub to -ininity to handle negative input arrays
        maxSub = float('-inf')
        # initialize the running sum of the current subarray
        currSum = 0
        # iterate through each number in the array
        for i in nums:
            # if current sum is negative, better start off fresh
            # reset currSum back to 0
            if currSum < 0:
                currSum = 0
            # add current number to currSum after removing negative prefix
            currSum += i
            # update the current max. subarray
            maxSub = max(maxSub, currSum)
        
        return maxSub
'''
Test Case
nums = [-2,1,-3,4,-1,2,1,-5,4]
Output
6
'''