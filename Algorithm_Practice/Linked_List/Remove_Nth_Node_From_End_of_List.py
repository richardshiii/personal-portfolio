'''
19. Remove Nth Node From End of List
Difficulty: Medium
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''
# Solution
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # T: O(n): iterate through the input linked list
        # S: O(1): no extra space needed, as remove is done in-place
        # use dummy node to handle edge cases and set up two pointers
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy
        # ahead pointer moves n+1 steps before moving the behind pointer
        for i in range(0, n + 1):
            ahead = ahead.next
        # the distance between ahead and behind pointers are n
        # behind pointer points to the node to be removed
        while ahead:
            ahead = ahead.next
            behind = behind.next
        # remove the nth node from the end of the list
        behind.next = behind.next.next
        return dummy.next        
'''
Test Case
head = [1,2,3,4,5]
n = 2
Output
[1,2,3,5]
'''