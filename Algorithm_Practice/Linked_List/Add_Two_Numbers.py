'''
2. Add Two Numbers
Difficulty: Medium
https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Solution
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_values = []
        l2_values = []
        #store value of each node as a char in a list
        #reverse the list and join each value to get the number
        curr = l1
        while curr:
            l1_values.append(str(curr.val))
            curr = curr.next
        l1_values = l1_values[::-1]
        l1_nums = int(''.join(l1_values))
        #store value of each node as a char in a list
        #reverse the list and join each value to get the number
        curr = l2
        while curr:
            l2_values.append(str(curr.val))
            curr = curr.next
        l2_values = l2_values[::-1]
        l2_nums = int(''.join(l2_values))
        #get the sum of two numbers
        #turn each digit into str and reverse to get value of each node
        new_digits = str(l1_nums + l2_nums)[::-1]
        #dummy node to point at the head of output linked list
        #add each digit to the output linked list
        #return dummy.next
        dummy = ListNode()
        curr = dummy
        for i in new_digits:
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy.next

'''
Test Case
l1 = [2,4,3]
l2 = [5,6,4]
Output
[7,0,8]
'''