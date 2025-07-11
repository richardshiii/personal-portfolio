'''
228. Summary Ranges
Difficulty: Easy
https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''
# Solution
class Solution:
    def summaryRanges(self, nums):
        # T: O(n): iterate through the input array
        # S: O(n): use ans[] to store output; 
        # if output does not count towards extra space, then O(1)
        # use empty array to store ans, set i to 0
        ans = []
        i = 0
        # iterate through the array to process each value
        while i < len(nums):
            start = nums[i]
            # make sure i is not out of bound;
            # expands the current range if consecutive number is found
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            # if the start point does not equal to nums[i]
            # the pointer moved forward and we have a range
            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i]))
            else:
                # single number range
                ans.append(str(start))
            # after recording a range, move i forward to test next value
            i += 1

        return ans

'''
Test Case
nums = [0,1,2,4,5,7]
Output
["0->2","4->5","7"]
'''