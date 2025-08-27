'''
14. Longest Common Prefix
Difficulty: Easy
https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''
# Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # T: O(m*n), m is the length of the shortest string, n is the number of strings in the input
        # S: O(1) no extra space required
        # set min_len to infinity and update later
        min_len = float('inf')
        # find the length of the shortest string
        # common prefix can't be longer than the shortest string
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        # initialize the pointer
        # compare each character of the strings 
        # use while loop to iterate through each input string & stop at min_len
        i = 0
        while i < min_len:
            # for each string in the input
            # make sure each string at index i are all matching 
            # return the substring up to i because at index i they are not matching
            # the part before i is the longest common prefix
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            # increment the pointer to check next character
            i += 1
        return strs[0][:i]

'''
Test Case
strs = ["flower","flow","flight"]
Output
"fl"
'''