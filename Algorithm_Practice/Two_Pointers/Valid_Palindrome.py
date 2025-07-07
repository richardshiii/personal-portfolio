'''
125. Valid Palindrome
Difficulty: Easy
https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''
# Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return ture if input string is empty
        if not s:
            return True
        # use isalnum() function to check whether all characters in the input 
        # string are alphanumeric
        # build an empty string to store checked character
        res = ""
        for char in s:
            if char.isalnum():
                res += char.lower()
        # compare the result string and its reverse
        # if same, then the input string is valid palindrome
        if res == res[::-1]:
            return True
        else:
            return False
'''
Test Case
"A man, a plan, a canal: Panama"
Output
true
'''