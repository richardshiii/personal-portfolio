'''
3. Longest Substring Without Repeating Characters
Difficulty: Medium
https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
# Solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # T: O(n) each character is visited at most twice (add & remove)
        # S: O(n) use char_set to store characters
        if len(s) == 0:
            return 0
        # initialize left pointer 
        # max_length to track maximum length found
        # char_set to store unique characters in current window
        l = 0
        max_length = 0
        char_set = set()
        # right pointer iterate through the input string
        # if current character is already in the set (duplicate)
        # shrink the window by moving the left pointer until duplicate is removed
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            # s[r] is guranteed to be a unique character, add it to the set
            # update the max_length window
            max_length = max(max_length, r-l+1)
            char_set.add(s[r])
        return max_length 
    
'''
Test Case
s = "abcabcbb"
Output
3
'''