'''
796. Rotate String
Difficulty: Easy
https://leetcode.com/problems/rotate-string/

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
 
Example:
Input: s = "abcde", goal = "cdeab"
Output: true
'''
# Solution
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # T: O(n^2): loop runs n time, each run we compare strings, which is also O(n)
        # S: O(1): no extra space required
        # edge case: if lengths are not equal, return False
        if len(s) != len(goal):
            return False
        # iterate through the string, and rotate the string by 1 character each time
        for i in range(len(s)):
            s = s[1:] + s[0]
            # compare the rotated string with goal
            if s == goal:
                return True
        # return False if no match found after all rotations
        return False
'''
Test Case
s = "abcde", goal = "abced"
Output
False
'''