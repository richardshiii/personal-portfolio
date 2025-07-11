'''
49. Group Anagrams
Difficulty: Medium
https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
'''
# Solution
class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        # T: O(n*m*26)
        # n is the number of words in the strs, m is the avg. length of each word
        # build character count for each word 
        # create a dictionary with key & value set as list
        res_dict = defaultdict(list)
        # iterate through each word in the input list
        for word in strs:
            # create a count lsit if size 26 initialized to 0 (26 characters)
            count = [0] * 26
            # Use ASCII values to find correct index: 'a' → 0, 'b' → 1, ..., 'z' → 25
            for char in word:
                count[ord(char) - ord('a')] += 1   
            # convert the list into a tuple so it can be used as a key in dictionary
            # This tuple uniquely represents the "character makeup" of the word
            key = tuple(count)
            # append the word to the list corresponding to its character-count key
            res_dict[key].append(word)
        
        # return grouped anagrams as a list
        return list(res_dict.values())
'''
Letters:     e a t
Count:       [1, 0, 0, 0, 1, 0, ..., 1, ..., 0]  # 'a'=1, 'e'=1, 't'=1
Tuple Key:   (1, 0, 0, 0, 1, ..., 1, ..., 0)
res_dict → {
    (1,0,0,...,1,...,1,...): ["eat"]
}
Letters:     t e a
Same key:    (1, 0, 0, 0, 1, ..., 1)
res_dict → {
    (1,0,0,...,1,...,1,...): ["eat", "tea"]
}
'''    
'''
Test Case
strs = ["eat","tea","tan","ate","nat","bat"]
Output
[["eat","tea","ate"],["bat"],["tan","nat"]]
'''