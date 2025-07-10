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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        #T: O(n*m*26) m为str里字符串的个数; n为str里每个字符串的平均长度; count array长度为26
        #建立一个dict,key和value都默认为list
        res_dict = defaultdict(list)
        #记录strs里每一个单词的字母count,字母count相同的单词互为anagram
        for word in strs:
            #count包含26个0,每个0用来记录一个字母的count
            count = [0] * 26
            #把每个word里的字母转换成ascii码,减去a的ascii码并计算出该字母的count
            for char in word:
                count[ord(char) - ord('a')] += 1

            #因为list不能作为dict的key,把list转为tuple解决该问题
            #dict的key为每个word的字母count    
            key = tuple(count)
            #dict的value为有相同字母count的word的集合
            res_dict[key].append(word)
        
        #输出结果要求为list
        return list(res_dict.values())
    
'''
Test Case
strs = ["eat","tea","tan","ate","nat","bat"]
Output
[["eat","tea","ate"],["bat"],["tan","nat"]]
'''