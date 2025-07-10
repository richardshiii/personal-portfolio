'''
209. Minimum Size Subarray Sum
Difficulty: Medium
https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''
# Solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # T: O(n) each element is visited at most twice by the pointers
        # S: O(1) no extra space is needed
        # set summ to 0
        # left pointer starts at the left side, and set min_length to +inf
        # to record the smallest valid window
        summ = 0
        min_length = float('inf')
        l = 0
        # move right pointer through the array and expand window by adding up nums[r]
        for r in range(len(nums)):
            summ += nums[r]
            # update the window when it still meets or exceeds the target value
            while summ >= target:
                # update the min_length and select the smaller window
                min_length = min(min_length, r-l+1)
                # shrink the window by substracting the leftmost value and moving the left pointer
                summ -= nums[l]
                l += 1
        # return the length of valid window if exists, otherwise return 0
        if min_length < float('inf'):
            return min_length
        else:
            return 0
'''
Test Case
target = 7
nums = [2,3,1,2,4,3]
Output
2
'''