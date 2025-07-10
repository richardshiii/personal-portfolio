'''
242. Valid Anagram
Difficulty: Easy
https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

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
        #anagrams: two words must have the same length
        #each char must be used only once
        #order of char can be different
        # vile <-> evil; anagram <-> nagaram
        
        s_counter = {}
        t_counter = {}
        #如果两个string长度不等直接返回False
        if len(s) != len(t):
            return False
        #string长度相等 遍历任意string都可以
        for i in range(len(s)):
            #哈希表的key为s和t里的每个字母, value是字母的count 
            #如果该字母已经存在,count在之前的数值上+1,否则设为0
            s_counter[s[i]] = 1 + s_counter.get(s[i], 0)
            t_counter[t[i]] = 1 + t_counter.get(t[i], 0)
        #对于两个哈希表内的字母及其count:
        #如果对应字母的count不相等就返回False
        #使用get()函数避免key error: 如果字母在t中不存在就替换为0
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