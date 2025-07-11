'''
57. Insert Interval
Difficulty: Medium
https://leetcode.com/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
'''
# Solution
class Solution:
    def insert(self, intervals):
        # T: O(n) iterate through the input interval
        # S: O(n) if counting output memory

        res = []

        for i in range(len(intervals)):
            # if the new interval's last value is smaller than the 1st value in input
            # append to res
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i: ]
            # if the new interval's first value is larger than the 1st value in input
            # can only be sure that the 1st interval can be appended 
            # need to compare newInterval with latter intervals
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # else there is overlapping
            # newInterval = min(left value of 2 intervals), max(right value of 2 intervals)
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), \
                                max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res

'''
Test Case
intervals = [[1,3],[6,9]]
newinterval = [2,5]
Output
[[1,5],[6,9]]
'''