'''
92. Reverse Linked List II
Difficulty: Mdeium
https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
'''
# Solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        # T: O(n): iterate through the input list once to find L & R positions
        # S: O(1): no extra needed since reverse in-place
        # use dummy node to handle edge case like reversing at position 1
        dummy = ListNode()
        dummy.next = head
        # two pointers: curr at head, left_prev 1 step before curr
        curr = head
        left_prev = dummy
        # get to the node at position L
        for i in range(0, left - 1):
            left_prev = curr
            curr = curr.next
        # reverse nodes between L and R (R - L + 1)
        # curr is at L position, leftprev at node before curr
        # use prev to help to reverse the section
        prev = None
        for i in range(0, right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # after reverse, curr is at the node after R
        # prev is at the node R 
        # connect the tail of the reversed list to the rest of the list
        left_prev.next.next = curr
        # connect the node before left to the new head of the list
        left_prev.next = prev
        # return dummy.next to skip the dummy node
        return dummy.next
        
'''
Test Case
head = [1,2,3,4,5]
left = 2
right = 4
Output
[1,4,3,2,5]
'''