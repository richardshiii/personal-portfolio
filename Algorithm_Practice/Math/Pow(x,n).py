'''
50. Pow(x,n)
Difficulty: Medium
https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n)

Example:
Input: x = 2.00000, n = 10
Output: 1024.00000
'''
# Solution
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # T: O(logn) divide n by 2 in each step
        # S: O(logn) recursive stack
        # if n == 0 -> return 1
        # if n < 0 -> x^n = 1/x^n
        # if n is even -> x^n = x^n/2 * x^n/2
        # if n is odd -> x^n = x * x^n/2 * x^n/2
        def helper(x, n):
            # edge cases
            if n == 0:
                return 1
            if x == 0:
                return 0
            # x^n = x^n/2 * x^n/2
            # if n is odd, return x * x^n/2 * x^n/2
            half = helper(x, n // 2)
            res = half * half
            # if n is odd, multiply one more x
            return x * res if n % 2 == 1 else res
        # input abs(n) to deal with -n cases
        # same calculation, just turn res to 1/res if n < 0
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res
'''
Test Case
x = 2.10000
n = 3
Output
9.26100
'''