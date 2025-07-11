'''
150. Evaluate Reverse Polish Notation
Difficulty: Medium
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''
# Solution
class Solution:
    def evalRPN(self, tokens):
        # T: O(2n) = O(n) reading each element, adding/removing each element 
        # S: O(n): use stack to store element from the input
        stack = []
        # iterate through every character in the input tokens
        for c in tokens:
            # +: pop previous two characters and add them together
            # append the result to the stack
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            # order matters for subtraction & division
            # subtract the last value from its previous
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            # *: pop previous two characters and multiply them together
            # append the result to the stack
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            # order matters for subtraction & division
            # divide the last value from its previous
            elif c == "/":   
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  
            # if c is not an operator -> number
            # append int(c) to the stack    
            else: 
                stack.append(int(c)) 
        return stack[0]
'''
Test Case
tokens = ["4","13","5","/","+"]
Output
6
'''