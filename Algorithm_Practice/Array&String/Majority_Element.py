'''
169. Majority Element
Difficulty: Easy
https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
# Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # T:O(n); S:O(1)
        # using Boyer-Moore Majority Vote Algorithm:
        # if an element appears more than half the time, all other elements combined cannot
        # outnumber it -- cancel out other elements using a counter
        
        ans = 0 # holds current majority element candidate
        count = 0 # tracks how confident we are that ans is the majority element

        for i in nums:
            # if count drops to 0, then current element can be the majority candidate
            if count == 0:
                ans = i
            # if the number matches current candidate, increase the count
            # otherwise, decrease the count 
            if ans == i:
                count += 1
            else:
                count -= 1
        # since majority element exists, ans after iterating through the input array must be 
        # the majority element
        return ans
    
'''
Test Case
nums = [3,2,3]
Output
3
'''