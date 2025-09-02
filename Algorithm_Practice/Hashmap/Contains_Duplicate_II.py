'''
219. Contains Duplicate II
Difficulty: Easy
https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums and an integer k, return true if there are two distinct indices 
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example:
Input: nums = [1,2,3,1], k = 3
Output: true
'''
# Solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # T: O(n): traverse the input array once
        # S: O(k): store at most k elements in the set
        # sliding window approach
        values = set()
        l = 0
        # iterate through the input array and expand the window
        for r in range(len(nums)):
            # if window size exceeds k, shrink window by moving left pointer to the right
            if r-l > k:
                # remove the leftmost element from the set
                values.remove(nums[l])
                l += 1
            # if the rightmost element is already in the set, then there is a duplicate
            # and and condition of i-j <= k is satified
            if nums[r] in values:
                return True
            # else, add the rightmost element to the set
            values.add(nums[r])
        # return False if no duplicates are found within the boundary
        return False

'''
Test Case
nums = [1,2,3,1,2,3], k = 2
Output
False
'''