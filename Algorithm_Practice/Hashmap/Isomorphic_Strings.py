'''
205. Isomophic Strings
Difficulty: Easy
https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to the same character, 
but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
'''
# Solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # T: O(2n) = O(n) iterate through both strings
        # S: O(n) use 2 hashmaps to store characters
        # create 2 hashmaps to track mapping
        mapST = {}
        mapTS = {}
        # use i to iterate through both input strings since the length of 
        # two strings must equal
        for i in range(len(s)):
            cs = s[i] # character from s at index i
            ct = t[i] # character from t at index i
            # check for inconsistent mapping:
            # Case 1: If character cs was already mapped to another character in t
            #         and that mapping doesn't match ct → conflict
            # Case 2: If character ct was already mapped to another character in s
            #         and that mapping doesn't match cs → conflict
            if ((cs in mapST and mapST[cs] != ct) \
            or (ct in mapTS and mapTS[ct] != cs)):
                return False

            # If no conflict, update both mappings to record current character pair
            mapST[cs] = ct
            mapTS[ct] = cs
        # If loop completes without conflict, the strings are isomorphic
        return True

'''
Test Case
s = "foo"
t = "bar"
Output
False
'''