'''
149. Max Points on a Line
Difficulty: Hard
https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.

Example:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
'''
# Solution
from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # for each point, determine if it lies on the longest line
        # count all points with the same slope (y2-y1)/(x2-x1)
        # at minimum, 1 point is always on the line
        res = 1
        # iterate through all points
        for i in range(len(points)):
            # determine whether this point is on the longest line
            p1 = points[i]
            # use hashmap to record and count slope
            count = defaultdict(int)
            # iterate through other points
            for j in range(i + 1, len(points)):
                p2 = points[j]
                # if two points have the same x coordinates -> vertical line
                if p2[0] == p1[0]:
                    slope = float('inf')
                else:
                    # calculate slope b/t two points
                    slope = (p2[1] - p1[1])/(p2[0] - p1[0])
                # update count since we found a point on the line with the same slope
                count[slope] += 1
                res = max(res, count[slope] + 1) # number of points on the line + the original point
        
        return res
'''
Test Case
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output
4
'''