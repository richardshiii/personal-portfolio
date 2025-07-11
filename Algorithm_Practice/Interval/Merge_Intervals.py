'''
56. Merge Intervals
Difficulty: Medium
https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''
# Solution
class Solution:
    def merge(self, intervals):
        # T: O(n log n) due to sorting in place, n is the number of intervals in the input
        # S: O(n)
        # sort input interval in place
        intervals.sort(key = lambda interval: interval[0])
        merged = []
        # iterate through each interval
        for i in intervals:
            # if merged list is empty or no overlap with the last interval in merged
            if not merged or merged[-1][1] < i[0]: 
                # No overlap → safely append current interval
                merged.append(i)
            # else there is a overlap
            else: 
                # modify the last merged interval
                # left value is the first value from previous merged interval
                # right value is the max b/t last value of the two intervals
                # -> [1, 3], [3, 6] -> [1, 6]
                merged[-1] = [merged[-1][0], max(merged[-1][-1], i[-1])]
        
        return merged
                

'''
Test Case
intervals = [[1,4],[4,5]]
Output
[[1,5]]
'''