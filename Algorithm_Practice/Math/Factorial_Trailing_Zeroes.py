'''
172. Factorial Trailing Zeroes
Difficulty: Medium
https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero
'''
# Solution
class Solution:
    def trailingZeroes(self, n):
        # T: O(log_5 n) divided by 5 repeatedly
        # S: O(1) only a few integer variables are used

        # trailing 0 is caused by factor of 10
        # 10 = 2 * 5, and factors of 2 contribute more to the factorials than factors of 5->(more even numbers)
        # trailing 0 is linked to number of factors of 5
        # so we count the number of factors of 5 in n!
        # n = n // 5 until n < 5; record n
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count
'''
Test Case
n = 5
Output
1
'''