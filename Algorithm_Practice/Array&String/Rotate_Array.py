'''
189. Rotate Array
Difficulty: Medium
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
# Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Do not return anything, modify nums in-place instead."""
        # T: O(n): iterate through the input array a constant number of times
        # S: O(1): in-place reversal, no extra space required
        # k % len(nums) in case k > len(nums)
        k = k % len(nums)
        # step 1: reverse the entire input array
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # step 2: reverse the first k elements
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # step 3: reverse the remaining elements
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

'''
Test Case
nums = [1,2,3,4,5,6,7]
k = 3
Output
[5,6,7,1,2,3,4]
'''