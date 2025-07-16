'''
148. Sort List
Difficulty: Medium
https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150

Given the head of a linked list, return the list after sorting it in ascending order.

Example:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
'''
# Solution
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head):
        # Merge Sort for Linked List
        # T: O(n log n) — each split is O(log n), each merge is O(n)
        # S: O(log n) — due to recursion stack (not creating new nodes)
        # base case: empty list or single node is already sorted
        if not head or not head.next:
            return head
        # split input linked list into two halves
        left = head # left pointer at head node
        right = self.getMid(head) #right pointer at the mid point
        tmp = right.next # use tmp to store right half
        right.next = None # cut the linked list at mid 
        right = tmp
        # recursively sort each half
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head):
        # Fast and slow pointer to find the midpoint
        # fast moves 2 steps at a time, slow moves 1
        slow, fast = head, head.next
        # by the time fast reaches end, slow pointer is at the mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left, right):
        # merge two sorted linked list
        # tail points to the last node in the sorted list
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        # append any remaining nodes
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next
        
'''
Test Case
head = [-1,5,3,4,0]
Output
[-1,0,3,4,5]
'''