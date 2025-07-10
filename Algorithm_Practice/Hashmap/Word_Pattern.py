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
        #T: O(len(s+pattern)) 需要遍历s和pattern
        #S: O(len(s+pattern)) 2个hash map
        #把s以空格为分隔符切开,每个单词对应pattern中的一个字母
        words = s.split(" ")
        #如果pattern和words长度不等 不可能match 直接return False
        if len(pattern) != len(words):
            return False
        #建立两个空的哈希表储存mapping
        WtP = {}
        PtW = {}
        #因为pattern和words长度一定相同 所以只用遍历一个就行
        for i in range(len(pattern)):
            w = words[i]
            p = pattern[i]
            #确保word/pattern已经在对应的哈希表内 如果该字符的mapping已经对应了一个不同的字符 
            #返回False
            if w in WtP and WtP[w] != p:
                return False
            if p in PtW and PtW[p] != w:
                return False
            #如果是新的字符或者已存在的字符和其对应的mapping,都可以更新哈希表
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