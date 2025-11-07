'''
88. Merge Sorted Array
Difficulty: Easy
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
# Solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # T: O(m+n) every element from both arrays are checked once
        # S: O(1) modification is done in-place, no extra space needed
        # lastIndex represents the last index & length of the merged array
        # x, y represents the length of nums1 and nums2, respectively
        # -1 to accomodate 0-based indexing in Python
        lastIndex = m + n - 1
        x = m - 1
        y = n - 1
        # iterate from the end of the merged array
        for z in range(lastIndex, -1, -1):
            # if nums1 has no elements left, merge the rest of nums2 into nums1
            # and move y one place to the left
            # check boundary condition first to avoid index error
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
            # if nums2 has no elements left, then the merging is complete, break the loop
            elif y < 0:
                break
            # if nums1 and nums2 are not empty, then compare value at each index,
            # place the larger integer at the end of the merged array
            # and move corresponding pointer 1 place to the left
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            elif nums1[x] <= nums2[y]:
                nums1[z] = nums2[y]
                y -= 1

'''
Test Case
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Output
[1,2,2,3,5,6]
'''