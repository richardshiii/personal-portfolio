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
        #T: O(n); S: O(n)
        #用哈希表记录nums里元素的value和index 
        #val : index
        hash = {}
        #针对nums中的每一个数字:
        #计算target - num 并在哈希表中寻找这个数值存不存在
        #如果存在,找出它的index并返回
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [i, hash[diff]]
            #如果在已存在的哈希表中没有找到diff,把下一个值和其index加入哈希表
            hash[num] = i    

'''
Test Case
nums = [3,2,4]
target = 6
Output
[2,1]
'''    