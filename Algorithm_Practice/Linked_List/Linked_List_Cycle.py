'''
141. Linked List Cycle
Difficulty: East
https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''
# Solution
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # T: O(n) traverse the full linked list
        # S: O(1) no extra space needed
        # Floyd's Cycle Detection Algorithm (Toitorse & Hare)
        # create dummy node and point to the head node
        dummy = ListNode()
        dummy.next = head
        # initialize two pointers at head node
        fast = slow = head
        # traverse the linked list until the fast pointer reaches the end
        while fast and fast.next:
            # fast pointer moves two steps at a time 
            # while slow pointer moves one step at a time
            fast = fast.next.next
            slow = slow.next
            # if cycle exists, fast pointer will catch the slow pointer eventually
            if fast == slow:
                return True
        # otherwise, no cycle detected
        return False
    
'''
Test Case
head = [3,2,0,-4]
pos = 1
Output
True
'''