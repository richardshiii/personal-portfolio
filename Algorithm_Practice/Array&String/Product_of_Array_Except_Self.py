'''
238. Product of Array Except Self
Difficulty: Medium
https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''
# Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two-passes solution
        # T: O(n): iterate through the input array twice
        # S: O(1): the output array does not count as extra space
        # create the result array
        res = [1] * len(nums)
        # set up prefix and postfix
        prefix = 1
        postfix = 1
        # first pass: calculate the prefix product
        # store the prefix product in the result array at the position i
        for i in range(len(nums)):
            res[i] = prefix
            # update the prefix by mulplying prefix with current value at nums[i]
            prefix *= nums[i]
        # second pass: calculate the postfix product
        # since in the first pass we already stored prefix product in the result array,
        # we can directly multuply the postfix product to the result array at i
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i] 

        return res

'''
Test Case
nums = [1,2,3,4]
Output
[24, 12, 8, 6]
'''