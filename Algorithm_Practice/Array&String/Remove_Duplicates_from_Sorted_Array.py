'''
26. Remove Duplicates from Sorted Array
Difficulty: Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
# Solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        # T: O(n)
        # S: O(1) no extra space is used
        # handle edge case: empty array
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            # only move the right pointer when a unique number is found
            # i: search for next unique number
            # j: track last unique number's position
            if nums[i] != nums[i - 1]:
                # move to the next position for uniqle number
                j += 1 
                # overwrite at position j
                nums[j] = nums[i]
                    
        return j+1
        '''
        exist = set()
        res = 0

        for num in nums:
            if num not in exist:
                nums[res] = num
                res += 1
                exist.add(num)
        return res

'''
Test Case
nums = [1,1,2]
Output
[1,2]
'''