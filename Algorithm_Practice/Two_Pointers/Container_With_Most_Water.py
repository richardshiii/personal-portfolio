'''
11. Container with Most Water
Difficulty: Medium
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
# Solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # T: O(n) each element is visited once at most
        # S: O(1) no extra space needed except for max_area calculation
        # Use two pointers, left pointer at the start of input array, 
        # right pointer at the end of input array
        # set max_area to 0 and update during iteration
        l = 0
        r = len(height) - 1
        max_area = 0
        # use while loop to break the loop when two pointers meet
        while l < r:
            # width equals r - l
            # height is the smaller value between height[l] and height[r]
            # max_area = w * h, and update max_area after every iteration
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            max_area = max(max_area, a) 
            # the area is limited by the shorter height
            # so we move the pointer pointing to the shorter height towards the other side
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
    
'''
Test Case
height = [1,8,6,2,5,4,8,3,7]
Output
49
'''