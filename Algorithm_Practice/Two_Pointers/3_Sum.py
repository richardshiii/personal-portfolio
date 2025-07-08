'''
15. 3Sum
Difficulty: Medium
https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''
# Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return 3 indices that are distinct and corresponding values sum up to be 0
        # no duplicate triplets
        # for each element in the input array, use two pointers to find two elements after,
        # and check the sum of triplet
        # S: O(1) sort in-place
        # T: O(n^2) while loop inside for loop
        #sort input array in place for easier implementation of two pointers
        nums.sort()
        ans = []
        # if nums[i] > 0, since the input array is sorted, it is impossible to 
        # get negative values to get 0, so break the loop
        # skip duplicate values for nums[i] to avoid duplicate triplets
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            # use two pointers, one placed after i, and one at the end of input array
            low = i + 1
            high = len(nums) - 1
            # break the loop if two pointers meet
            while low < high:
                # calculate the sum of current triplet
                summ = nums[i] + nums[low] + nums[high]
                # if valid, add the triplet to ans, and move pointers inward
                if summ == 0:
                    ans.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    # skip duplicate for the low pointer
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    # skip duplicate for the high pointer
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                # if the sum < 0, move left pointer to the right to increase sum
                # otherwise, move right pointer to the left to decrease sum 
                elif summ < 0:
                    low += 1
                else:
                    high -= 1
        return ans

'''
Test Case
nums = [-1,0,1,2,-1,-4]
Output
[[-1,-1,2],[-1,0,1]]
'''