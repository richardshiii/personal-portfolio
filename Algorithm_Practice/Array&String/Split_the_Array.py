'''
3046. Split the Array
Difficulty: Easy
https://leetcode.com/problems/split-the-array/

You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:
nums1.length == nums2.length == nums.length / 2.
nums1 should contain distinct elements.
nums2 should also contain distinct elements.
Return true if it is possible to split the array, and false otherwise.

Example:
Input: nums = [1,1,2,2,3,4]
Output: true
Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].
'''
# Solution
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # set up a counter to count the frequencyy of each number in the array
        c = Counter(nums)
        # the frequency of each number can't exceed 2
        # otherwise it is impossible to split the array
        for i in c:
            if c[i] > 2:
                return False
        return True

'''
Test Case
nums = [1,1,2,2,3,4]
Output
True
'''