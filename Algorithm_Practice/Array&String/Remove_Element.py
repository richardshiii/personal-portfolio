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
        # Use two pointers to iterate through the array;
        # Use while loop to break the loop when the two pointers meet;
        # When nums[left] == val, replace it with the last unchecked element (nums[right - 1]), 
        # move right pointer back 1 step.
        # Otherwise, increment left pointer       
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else: left += 1
        return right
    
'''
Test Case
[3,2,2,3], val = 3
Output
[2,2]
'''