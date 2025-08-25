'''
55. Jump Game
Difficulty: Medium
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
# Solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # T: O(n): traverse the input array once
        # S: O(1): no extra space required
        # start with 0 gas
        gas = 0
        # iterate through the array
        for i in range(len(nums)):
            # return False if gas is negative (can't reach further more)
            if gas < 0:
                return False
            # if current index has more gas then what's left, update gas amount
            elif i > gas:
                gas = i
            # decrease gas by 1 for each step
            gas -= 1
        # if we can reach the end of the array, then return True
        return True
    '''
    goal = len(nums) - 1

        for i in range(goal - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        if goal == 0:
            return True
        else:
            return False

    '''

'''
Test Case
nums = [2,3,1,1,4]
Output: True
'''