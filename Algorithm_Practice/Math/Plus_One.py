'''
66. Plus One
Difficulty: Easy
https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150

You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4]
'''
# Solution
class Solution:
    def plusOne(self, digits):
        # T: O(n) iterate through the entire input array
        # S: O(1) no extra memory needed
        # reverse input array for easier process
        digits = digits[::-1]
        carry = 1
        # initialize the index to traverse the reversed number
        i = 0
        # keep looping until carry becomes 0
        while carry == 1:
            if i < len(digits):
                # if digit is 9 then turn it to 0 -> 9+1 = 10 & carry is still 1
                if digits[i] == 9:
                    digits[i] = 0
                # if digit is not 9, then increment by 1 and set carry to 0
                else:
                    digits[i] += 1
                    carry = 0
            # if i goes out of bounds -> 999+1 = 1000
            # append 1 -> 1 more digit after reverse back
            # no more carry
            else:
                digits.append(1)
                carry = 0
            i += 1
        # reverse back to original digit order
        return digits[::-1]

'''
Test Case
digits = [4,3,2,1]
Output
[4,3,2,2]
'''