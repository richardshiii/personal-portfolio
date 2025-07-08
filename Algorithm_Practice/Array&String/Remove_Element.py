'''
27. Remove Element
Difficult: Easy
https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150 

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
# Solution
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # T: O(n) every element is checked at most once
        # S: O(1) no extra space is needed  
        left = 0
        right = len(nums)
        # Use two pointers to iterate through the array;
        # Use while loop to break the loop when the two pointers meet;
        while left < right:
            # when a target value is found, overwrite it with the last unchecked value
            if nums[left] == val:
                nums[left] = nums[right - 1]
                # shrink valid array range by 1
                # don't move left pointer since the overwritten value can also be target value
                right -= 1
            # only move left pointer if current value is not target value
            else: left += 1
        # return the new length of the array, all values after the right pointer can be ignored
        return right
    
'''
Test Case
[3,2,2,3], val = 3
Output
[2,2]
'''