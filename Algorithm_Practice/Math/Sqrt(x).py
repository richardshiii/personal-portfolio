'''
69. Sqrt(x)
Difficulty: Easy
https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
'''
# Solution
class Solution:
    def mySqrt(self, x: int) -> int:
        # T: O(logn): binary search halves the range each time
        # S: O(1): constant space used
        # Binary search: range from 0 to x
        l, r = 0, x
        res = 0
        # while two pointers do not intersect:
        while l <= r:
            # calculate the mid point
            mid = l + ((r - l) // 2)
            # case 1: mid squared is greater than x → need smaller numbers
            # check mid ** 2
            # if value > x, lower range to (l, m - 1)
            if mid ** 2 > x:
                r = mid - 1
            # case 2: mid squared is less than x → mid might be the answer, 
            # but check higher
            # if value < x, move left pointer to (mid + 1)
            # mid could be a solution
            elif mid ** 2 < x:
                l = mid + 1
                res = mid
            # case 3: mid squared equals x → exact square root found
            # if value == x, mid is the solution
            else:
                return mid
        return res
'''
Test Case
8
Output
2
'''