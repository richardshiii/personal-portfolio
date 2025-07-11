'''
224. Basic Calculator
Difficulty: Hard
https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150

Given a string s representing a valid expression, implement a basic calculator 
to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings 
as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2
'''
# Solution
class Solution:
    def calculate(self, s: str) -> int:
        output = 0 # stores running total outside the parentheses
        curr = 0 # build multi-digit numbers from characters 
        sign = 1 # tracks whether to add or subtract the current number
        stack = [] # stores previous result and signs when entering a new () context
        # Iterate through the input string
        for c in s:
            # case 1: digits
            # 31 -> 3*10+1
            if c.isdigit():
                curr = curr * 10 + int(c)
            # case 2: operators
            # process previous digits to the running total 
            elif c in '+-':
                # add previous number to the runnig total
                output += (curr * sign)
                # reset curr for the next number
                curr = 0
                # update sign based on current operator
                if c == "+":
                    sign = 1
                else:
                    sign = -1
            # case 3: '('
            # push current result and sign for later calculation
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                # reset output and sign for inner expression
                output = 0
                sign = 1
            # case 4: ')'
            # 
            elif c == ")":
                # add last number in parentheses
                output += (curr * sign)
                # apply sign before '('
                output *= stack.pop()
                # add result from before the '('
                output += stack.pop()
                # reset current number
                curr = 0
        # add remaining number to the result
        return output + (curr * sign)
    
'''
Test Case
s = " 2-1 + 2 "
Output
3
'''