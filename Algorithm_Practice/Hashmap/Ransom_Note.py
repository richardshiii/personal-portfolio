'''
383. Ransom Note
Difficulty: Easy
https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
'''
# Solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # T: O(len(ransom) + len(magazine)) -> loop through both inputs
        # S: O(magazine) -> only char from magazine are stored in hash map/dict
        # build hashmap
        mag = {}
        # iterate through magazine & record unique characters and count
        for char in magazine:
            if char in mag:
                mag[char] += 1
            else:
                mag[char] = 1
        # iterate through input note & compare characters with characters in the hashmap
        for char in ransomNote:
            # if no match, return False
            if char not in mag:
                return False
            # if character count is 1, delete from hashmap after matching
            elif mag[char] == 1:
                del mag[char]
            # of character count > 1, minus 1 after each match
            else:
                mag[char] -= 1
        # if all conditions are passed, return True
        return True

'''
Test Case
ransomNote = "aa"
magazine = "aab"
Output
True
'''