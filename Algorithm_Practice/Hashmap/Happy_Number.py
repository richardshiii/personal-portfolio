'''
202. Happy Number
Difficulty: Easy
https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150

Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
# Solution
class Solution:
    def isHappy(self, n: int) -> bool:
        # use a set to track numbers that have been seen
        # set: store collection of unique elements
        # haspmap: dictionary that stores key-value pairs
        seen = set()
        # stop the loop when we reach 1
        # if n is already in the set, we are in a cycle, return False
        while n != 1:
            if n in seen:
                return False
            # else, add n to the set
            else:
                seen.add(n)
            # calculate the sum of squares of the digits of n
            new_n = 0
            for digit in str(n):
                new_n += int(digit) ** 2
            n = new_n
        # return True if we reach 1 and meet all conditions 
        return True
    
'''
Test Case:
n = 19
Output
True
'''