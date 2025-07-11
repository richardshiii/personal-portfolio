'''
242. Valid Anagram
Difficulty: Easy
https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Anagram: a word or phrase formed by rearranging the letters of a different word or phrase, 
using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
'''
# Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams: two words must have the same length
        # each char must be used only once
        # order of char can be different
        # vile <-> evil; anagram <-> nagaram
        # use 2 hash tables (dictionaries) to count character frequency
        s_counter = {}
        t_counter = {}
        # return false if two input strings have different length
        if len(s) != len(t):
            return False
        # iterate through both input strings
        # count the frequency of each character in both strings
        for i in range(len(s)):
            # s[i] is the current charc. in string s
            # use get(key, default) to safely increament the frequency count
            s_counter[s[i]] = 1 + s_counter.get(s[i], 0)
            # count character frequency in string t 
            t_counter[t[i]] = 1 + t_counter.get(t[i], 0)
        # compare 2 hash maps
        # for each character counted in s, check the count in t
        # return false if frequency count is different 
        # otherwise return true (all character counts match)
        # use get(key, default) to set count to 0 for character that does not exist
        for char in s_counter:
            if s_counter[char] != t_counter.get(char, 0):
                return False
        return True
        
        #Solution 2:
        #return sorted(s) == sorted(t)

'''
Test Case
s = "anagram"
t = "nagaram"
Output
True
'''