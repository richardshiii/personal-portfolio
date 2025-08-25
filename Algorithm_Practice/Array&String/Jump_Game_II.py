'''
45. Jump Game II
Difficulty: Medium
https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

Example:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
# Solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        # T: O(n): iterate through the input array once
        # S: O(1): no extra space required
        # use greedy approach to find the minimum number of jumps required to reach the end
        # initialize jumps, farthest distance, left and right pointers
        jumps = 0
        farthest = 0
        l = r = 0
        # iterate through the input array until the right pointer is out of bound
        while r < len(nums) - 1:
            # find the farthest distance we can reach in current jump
            for i in range(l, r+1):
                # update farthest distance as the maximum of current farthest and i + nums[i]
                farthest = max(farthest, i + nums[i])
            # update left pointer to the right pointer + 1
            # update right pointer to the farthest distance we can reach
            l = r + 1
            r = farthest
            # increment jumps by 1
            jumps += 1
        # if we can reach the end of the array, return the number of jumps 
        return jumps
            
'''
Test Case
nums = [2,3,1,1,4]
Output 
2
'''