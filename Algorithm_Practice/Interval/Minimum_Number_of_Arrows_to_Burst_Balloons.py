'''
452. Minimum Number of Arrows to Burst Balloons
Difficulty: Medium
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150

There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] 
denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact 
y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the 
number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
'''
# Solution
class Solution:
    def findMinArrowShots(self, points):
        # T: O(n log n) sorting + O(n) interation = O(n log n)
        # S: O(n) if counting output space, else O(1)

        # sort input interval in ascending order
        points.sort()       
        # assume one arrow per ballon at the start
        res = len(points) 
        # track the current overlapping region
        prev = points[0]
        # iterate through the remaining balloons
        for i in range(1, len(points)):
            curr = points[i]
            # if there is a overlap between current and previous balloon
            # if curr[0] <= prev[1] -> overlap
            if curr[0] <= prev[1]:
                # reduce number of arrows by one since they can be burst by 1 arrow 
                # [1, 5], [2, 4] -> [1, 4]
                res -= 1 
                # only merge the overlapped region b/t 2 intervals
                prev = [curr[0], min(curr[1], prev[1])]
            # if no overlap, set previous interval to current interval, move forward
            else: 
                prev = curr
        
        return res

'''
Test Case
points = [[10,16],[2,8],[1,6],[7,12]]
Output
2
'''