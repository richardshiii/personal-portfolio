'''
155. Min Stack
Difficulty: Medium
https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''
# Solution
class MinStack:
    def __init__(self):
        # primary stack to store all values
        self.stack = []
        # min_stack to store the min. value at each level
        self.min_stack = []

    def push(self, val: int) -> None:
        # push value to the main stack
        self.stack.append(val)
        # if min_stack is empty, or val <= current min., 
        # push val as the new min. 
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] < val:
            # Push the current minimum again to maintain alignment
            self.min_stack.append(self.min_stack[-1])
        # val <= current min → val becomes new min
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop from both stacks to keep them aligned
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top of the min_stack (current minimum)
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
Test Case
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
'''