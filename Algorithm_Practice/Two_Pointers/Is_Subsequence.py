'''
392. Is Subsequence
Difficulty: Easy
https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''
# Solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # T: O(n) worst case scenario is iterating through t
        # S: O(1) no extra space is needed
        # Use two pointers to iterate from the start of s & t
        i = 0
        j = 0
        # Use while loop to iterate through each input string
        # if s[i] == t[j], then move both i and j to the right to compare the next character
        # if s[i] != t[j], then only move j to the right
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        # if s is a subsequence of j, all characters in s are matched, then len(s) must equal to i 
        # return True
        # otherwise return False
        if i == len(s):
            return True
        else:
            return False
        
'''
Test Case
s = "abc"
t = "ahbgdc"
Output
True
'''