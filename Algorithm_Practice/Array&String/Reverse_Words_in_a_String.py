'''
151. Reverse Words in a String
Difficulty: Medium
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example:
Input: s = "the sky is blue"
Output: "blue is sky the"
'''
# Solution
class Solution:
    def reverseWords(self, s: str) -> str:
        # T: O(n): iterate through the input string
        # S: O(n): store the reversed words in a list
        # split the input string by space, reverse order, 
        # and remove leading & trailing space
        str_list = ' '.join(s.split(' ')[::-1]).strip(' ')
        # initialize an empty list to store words
        res = []
        # iterate through the str_list and record the index & values
        for i, c in enumerate(str_list):
            # avoid multiple empty spaces
            # move index forward if encounter multiple spaces
            if i < len(str_list) - 1 and str_list[i] == str_list[i+1] == ' ':
                i += 1
            # else, append the word to the res list
            # increment the index to check next word
            else:
                res.append(c)
                i += 1
        # join the words together and return as a string
        return ''.join(res)

'''
Tetst Case
s = "  hello world  "
Output
"world hello"
'''