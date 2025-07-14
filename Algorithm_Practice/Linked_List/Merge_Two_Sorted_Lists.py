'''
21. Merge Two Sorted Lists
Difficulty: Ease
https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.
Return the head of the merged linked list.

Example
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
# Solution
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # T: O(n+m): iterate through both input lists
        # S: O(1): no extra space is needed
        # new_head is a dummy node acts as the head of the merged list
        new_head = ListNode()
        # curr is the moving pointer to build the merged list
        curr = new_head
        # iterate through both linked lists until one is exhausted
        while list1 and list2:
            # compare the current values of both lists
            # if list1's value is smaller, point curr.next to list1
            if list1.val < list2.val:
                curr.next = list1
                # move list1 to its next node 
                list1 = list1.next
            # else, point curr.next to list2 & move list2 to its next node
            else:
                curr.next = list2
                list2 = list2.next
            # Move curr to the node just added, preparing for the next link
            curr = curr.next
        # after the loop, one list may still have remaining nodes.
        # since the remaining nodes are already sorted, simply attach the rest.
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        # return the merged list, which starts at new_head.next()
        # skipping the dummy node
        return new_head.next
    
'''
Test Case
list1 = [1,2,4]
list2 = [1,3,4]
Output
[1,1,2,3,4,4]
'''