'''
1. Two Sum
Difficulty: Easy
https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
#Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # T: O(n): iterate the input nums once
        # S: O(n): worst case, store every number in nums in the hash table
        # use hash table to record value-index pairs
        # val : index
        hash = {}
        # for every element in nums and its index
        # calculate the difference between target number and current number
        # if the difference is in hash table, return its index together with i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff], i]
            # otherwise, store current number and its index in the hash map
            hash[num] = i    

'''
Test Case
nums = [3,2,4]
target = 6
Output
[2,1]
'''    