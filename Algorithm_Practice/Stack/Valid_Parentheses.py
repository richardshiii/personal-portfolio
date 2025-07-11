'''
20. Valid Parentheses
Difficulty: East
https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true
'''
# Solution
class Solution:
    def isValid(self, s: str) -> bool:
        # T: O(n) n = len(str)
        # S: O(n) use stack to store input elements
        # use stack to store left brackets
        stack = []
        # iterate through input and store left brackets in the stack
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                # edge case: if empty stack, meaning to left brackets, then 
                # the parentheses can't be closed -> return false
                if not stack:
                    return False
                # return false if next element can't match with last element in the stack
                if char == ')' and stack[-1] != '(' or \
                char == ']' and stack[-1] != '[' or \
                char == '}' and stack[-1] != '{' :
                    return False
                # if match, pop the left parentheses to check the next one
                stack.pop()  
        # if all elements match, stack should be empty at the end -> return True
        # otherwise return false
        if stack:
            return False
        else:
            return True

'''
Test Case
s = "()[]{}"
Output
True
'''