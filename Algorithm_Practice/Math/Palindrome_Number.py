'''
9. Palindrome Number
Difficulty: Easy
https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer x, return true if x is a palindrome 
(reads the same forward and backward), and false otherwise.

Example:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''
# Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # T: O(log n): compare half the digits
        # S: O(1): no extra space needed
        # -121 -> 121-
        if x < 0:
            return False
        # determine the divider value (10, 100, 1000, etc.,)
        # for the leftmost digit
        # 12321 -> divider = 10000
        divider_value = 1
        while x >= 10 * divider_value:
            divider_value *= 10
        # compare the left and right digit
        while x:
            right_digit = x % 10
            left_digit = x // divider_value
            # if not match, return False
            if left_digit != right_digit:
                return False
            # remove left and right digit from the number
            # x % divider_value to remove leftmost digit
            # // 10 remove rightmost digit
            x = (x % divider_value) // 10
            # update divider: / 100 since we get rid of 2 digits
            divider_value = divider_value / 100
        return True
'''
Test Case
x = -121
Output
False 
-121 -> 121-
'''