'''
58. Length of Last Word
Difficulty: Easy
https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
# Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # T: O(n): worst case we have to traverse the entire string backwards
        # S: O(1): no extra space required
        # edge case: return 0 if input string is empty
        if len(s) == 0:
            return 0
        # initialize pointer at the end of the string and counter
        i = len(s) - 1
        count = 0
        # deal with spaces: move pointer to the left if encounter empty space
        while s[i] == " ":
            i -= 1
        # make sure we are in bound and when encounter non-space character:
        # increase the counter by 1 and move pointer further left
        # 0-based index so i could be 0
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
        return count

'''
Test Case
s = "   fly me   to   the moon  "
Output
4
'''