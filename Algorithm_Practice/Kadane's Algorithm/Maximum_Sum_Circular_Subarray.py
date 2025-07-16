'''
918. Maximum Sum Circular Subarray
Difficulty: Medium
https://leetcode.com/problems/maximum-sum-circular-subarray/?envType=study-plan-v2&envId=top-interview-150

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. 
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, 
for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
'''
# Solution
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # T: O(n) iterate through input once
        # S: O(1) no extra memory needed

        # set globMax & globMin to the 1st value instead of 0
        # since globMax & globMin won't be updated until a greater value is found
        # and it is possible the 1st value is the one in case all values are negative
        globMax, globMin = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0
        # iterate through each element of the input array
        # calculate the max. subarray & min subarray (in case the max is circular)
        for n in nums:
            # Kadane's algorithm to calculate the maximum
            currMax = max(currMax + n, n)
            globMax = max(globMax, currMax)
            # calculate the minimum subarray
            currMin = min(currMin + n, n)
            globMin = min(globMin, currMin)
            # keep track of total sum for circular wrap cases
            total += n
        # If all numbers are negative, total - globMin would be zero
        # In that case, return globMax (the least negative number)
        # Return the larger between:
            # - globMax: max subarray that doesn't wrap
            # - total - globMin: max subarray that wraps (total - min sum subarray)
        return max(globMax, total - globMin) if globMax > 0 \
        else globMax
        # Edge case: all elements are negative → return the largest single element

'''
Test Case
nums = [1,-2,3,-2]
Output
3
'''