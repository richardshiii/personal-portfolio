'''
13. Roman to Integer
Difficulty: Easy
https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, 
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example:
Input: s = "III"
Output: 3
Explanation: III = 3.
'''
# Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        # T: O(n): iterate through the input string once
        # S: O(1): hash map has fixed size
        # create a hash map t store letter:value pairs
        hash = {"I":1, "V":5, "X":10, "L": 50,
                "C":100, "D":500, "M":1000}
        # initiate the result variable
        res = 0
        # iterate through the input string
        for i in range(len(s)):
            # make sure i+1 is within bounds
            # reference the hashmap to compare the current and next letter's value
            # to determine whether to add or subtract
            if i+1 < len(s) and hash[s[i]] < hash[s[i+1]]:
                res -= hash[s[i]]
            else:
                res += hash[s[i]]
        
        return res

'''
Test Case
s = "MCMXCIV"
Output
1994
'''