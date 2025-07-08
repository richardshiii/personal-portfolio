'''
80. Remove Duplicates from Sorted Array II
Difficulty: Medium
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
# Solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # T: O(n) iterate through the input once
        # S: O(1) modification is done in-place, no extra space needed
        if len(nums) == 0:
            return 0
        
        i = 1 #pointer used to substitute value
        dupCount = 1

        for j in range(1, len(nums)): #j is used to scan the array
            if nums[j] == nums[j - 1]:
                dupCount += 1
            else:
                dupCount = 1
            if dupCount <= 2:
                #both pointers start at index 1
                nums[i] = nums[j]
                #only increment sub pointer after substitution
                i += 1
        return i
                
'''
Test Case
nums = [1,1,1,2,2,3]
Output
[1,1,2,2,3]
'''