'''
290. Word Pattern
Difficulty: Easy
https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a 
letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".
'''
# Solution
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # T: O(len(s+pattern)) iterate through s and the patter 
        # S: O(len(s+pattern)) use 2 hash map to store word-pattern mapping
        # split s by space, so each word matchs with a character in the pattern
        words = s.split(" ")
        # if the length of pattern does not match the length of words, return false
        if len(pattern) != len(words):
            return False
        # use 2 hash tables to record mapping
        WtP = {}
        PtW = {}
        # use i to iterate through both inputs due to same length
        for i in range(len(pattern)):
            w = words[i]
            p = pattern[i]
            # return false if:
            # word/pattern already in hash map & current character has a different mapping
            if w in WtP and WtP[w] != p:
                return False
            if p in PtW and PtW[p] != w:
                return False
            # update the hash table if a new character and mapping is found
            WtP[w] = p
            PtW[p] = w

        return True

'''
Test Case
pattern = "abba"
s = "dog cat cat fish"
Output
False
'''